from calendar import HTMLCalendar

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