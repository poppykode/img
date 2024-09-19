from datetime import datetime, timedelta
import logging
from django.urls import reverse
from django.conf import settings
from calendar import HTMLCalendar
from core.email import Email
from .models import BookedMeeting


class Calendar(HTMLCalendar):
	# def __init__(self, year=None, month=None, user=None):
	# 	self.year , self.user = year, user
	# 	self.month = month
	# 	super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, meetings_):
		meetings_per_day = meetings_.filter(start_date__day=day)
		d = ''
		for meeting in meetings_per_day:
			d += f'<div class="tds-list-style mt-1">{meeting.start_date.strftime("%H:%M")} - {meeting.task_name} ({meeting.project.client.name})</div>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True, qs=None, y =None, m=None):
		meetings = qs 
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(y, m, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(y, m):
			cal += f'{self.formatweek(week, meetings)}\n'
		return cal
	
def meetings_due_for_check_in(minutes = 5):

	due_for_check_in = BookedMeeting.objects.to_check_in(minutes)
	logging.info(f"Time: {datetime.now()} ->> List of Due meeting for check in: {due_for_check_in}")
	base_url = settings.BASE_URL
	if due_for_check_in:
		for meeting in due_for_check_in:
			link  = reverse("meeting_calendar:check_in_or_check_out", kwargs={'meeting_id':meeting.id,'check_type':'check-in'})
			meeting.is_check_in = True
			meeting.save()
			email_ = Email(
				subject="Check In",
				recipient_list=[meeting.requester.email, meeting.requested.email],
				message=f"""
				<p>Check In</p>
				<p>Accepted by: {meeting.requested.get_full_name()} </p>
				<p>Requested by: {meeting.requested.get_full_name()} </p>
				<p>Slot: {meeting.booking_date}: {meeting.start_time} {meeting.end_time} </p>
				<a href={base_url}{link}>Click to check in</a>	 
				""",
			)
			print(email_)
			email_.send()

def meetings_due_for_check_out(minutes = 30):
	due_for_check_out = BookedMeeting.objects.to_check_out(minutes)
	logging.info(f"Time: {datetime.now()} ->> List of Due meeting for check out: {due_for_check_out}")
	base_url = settings.BASE_URL
	if due_for_check_out:		
		for meeting in due_for_check_out:
			link  = reverse("meeting_calendar:check_in_or_check_out", kwargs={'meeting_id':meeting.id,'check_type':'check-out'})
			meeting.is_check_out = True
			meeting.save()
			email_ = Email(
				subject="Check Out",
				recipient_list=[meeting.requester.email, meeting.requested.email],
				message=f"""
				<p>Check Out</p>
				<p>Accepted by: {meeting.requested.get_full_name()} </p>
				<p>Requested by: {meeting.requested.get_full_name()} </p>
				<p>Slot: {meeting.booking_date}: {meeting.start_time} {meeting.end_time} </p>
				<a href={base_url}{link}>Click to check out</a>	
				""",
			)
			email_.send()
