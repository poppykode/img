
import os
from datetime import datetime, date
# import plotly.express as px
# import pandas as pd
# from plotly.offline import plot

from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required



@login_required  
def candidate_dashboard(request):
    template_name = 'dashboards/candidate_dashboard.html'
    date_today = date.today()
    user = request.user
    # was_attended_no_res = models.Meeting.objects.filter(requester = user).filter(was_meeting_accepted=True).filter(was_meeting_attended = None).filter(date__lt = date_today)
    # user_ = get_object_or_404(models.User,id=user.id)
    return render(request, template_name)

@login_required  
def coach_dashboard(request):
    template_name = 'dashboards/coach_dashboard.html'
    date_today = date.today()
    user = request.user
    # user_ = get_object_or_404(models.User,id=user.id)
    # was_attended_no_res = models.Meeting.objects.filter(requested = user).filter(was_meeting_accepted=True).filter(was_meeting_attended = None).filter(date__lt = date_today)
    return render(request, template_name)

@login_required  
def admin_dashboard(request):
    template_name = 'dashboards/admin_dashboard.html'
    # meetings = Meeting.objects.all()
    # qs = models.User.objects.all()
    # accepted = len(qs.filter(is_coach=True).filter(account_status = 'accepted'))
    # pending = len(qs.filter(is_coach=True).filter(account_status = 'pending'))
    # rejected = len(qs.filter(is_coach=True).filter(account_status = 'rejected'))
    # values = [accepted, pending,rejected]
    names =  ["Accepted","Pending","Rejected"]
    # df = px.data.iris()
    # fig = px.pie(df,values=values, names=names)
    # pie_chart = plot(fig, output_type="div")
    # offers = Offer.objects.filter(status='pending')
    context ={
        # 'users':qs,
        # "pie_chart":pie_chart,
        # 'meetings':meetings,
        # 'offers':offers,
        # 'number_of_offers':len(offers)
    }
    return render(request, template_name,context)
