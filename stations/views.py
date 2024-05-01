from django.forms import formset_factory
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from core.decorators import role_required
from core.enums import (
    ExaminerMarkSheetEnum,
    RoleEnum
)
from . import forms
from . import models
from . import utils


# Create your views here.

## stations
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def first_level_stations(request):
    template_name = 'station/stations.html'
    first_level_stations_ = models.FirstLevelStation.objects.all()
    return render(request,template_name,{'items':utils.paginator(request,first_level_stations_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_first_level_station(request):
    template_name = 'station/create_station.html'
    form = forms.FirstLevelStationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"First level station successfully created.")
            return redirect('stations:first_level_stations')
    return render(request,template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_first_level_station(request, id):
    first_level_station_ = get_object_or_404(models.FirstLevelStation,id=id)
    form = forms.FirstLevelStationForm(request.POST or None, instance=first_level_station_)
    template_name = 'station/create_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'First level station {first_level_station_.title} successfully updated.')
            return redirect('stations:first_level_stations')
    return render(request, template_name, {'form':form,'type':'edit','obj':first_level_station_})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_first_level_station(request, id):
    first_level_station = get_object_or_404(models.FirstLevelStation,id=id)
    template_name = 'station/delete_station.html'
    if request.method ==  'POST':
        first_level_station.delete()
        messages.success(request,f'First level station {first_level_station.title} successfully deleted.')
        return redirect('stations:first_level_stations')
    return render(request, template_name, {'obj':first_level_station})

## stations categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def second_level_stations(request):
    template_name = 'station_category/station_categories.html'
    second_level_stations_ = models.SecondLevelStation.objects.all()
    return render(request,template_name,{'items':utils.paginator(request,second_level_stations_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_second_level_station(request):
    template_name = 'station_category/create_category_station.html'
    form = forms.SecondLevelStationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Second level station successfully created.")
            return redirect('stations:second_level_stations')
    return render(request,template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_second_level_station(request, id):
    second_level_station = get_object_or_404(models.SecondLevelStation,id=id)
    form = forms.SecondLevelStationForm(request.POST or None, instance=second_level_station)
    template_name = 'station_category/create_category_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'Second level station {second_level_station.title} successfully updated.')
            return redirect('stations:second_level_stations')
    return render(request, template_name, {'form':form,'type':'edit','obj':second_level_station})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_second_level_station(request, id):
    second_level_station = get_object_or_404(models.SecondLevelStation,id=id)
    template_name = 'station_category/delete_category_station.html'
    if request.method ==  'POST':
        second_level_station.delete()
        messages.success(request,f'Second level station {second_level_station.title} successfully deleted.')
        return redirect('stations:second_level_stations')
    return render(request, template_name, {'obj':second_level_station})

## stations sub categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def third_level_stations(request):
    template_name = 'station_sub_category/station_sub_categories.html'
    third_level_stations_ = models.ThirdLevelStation.objects.all()
    return render(request,template_name,{'items':utils.paginator(request,third_level_stations_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_third_level_station(request):
    template_name = 'station_sub_category/create_category_sub_station.html'
    form = forms.ThirdLevelStationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Second level station successfully created.")
            return redirect('stations:third_level_stations')
    return render(request,template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_third_level_station(request, id):
    third_level_station = get_object_or_404(models.ThirdLevelStation,id=id)
    form = forms.ThirdLevelStationForm(request.POST or None, instance=third_level_station)
    template_name = 'station_sub_category/create_category_sub_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'Second level station {third_level_station.title} successfully updated.')
            return redirect('stations:third_level_stations')
    return render(request, template_name, {'form':form,'type':'edit','obj':third_level_station})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_third_level_station(request, id):
    third_level_station = get_object_or_404(models.ThirdLevelStation,id=id)
    template_name = 'station_sub_category/delete_sub_category_station.html'
    if request.method ==  'POST':
        third_level_station.delete()
        messages.success(request,f'Second level station  {third_level_station.title} successfully deleted.')
        return redirect('stations:third_level_stations')
    return render(request, template_name, {'obj':third_level_station})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def station_creator(request):
    template_name = 'station_creator.html'
    form_candidate_ = formset_factory(forms.CandidateInstructionForm,extra=4)
    form_patient_ = formset_factory(forms.PatientDisclosureForm, extra = 3)
    form_station = forms.StationForm(request.POST or None)
    form_candidate = form_candidate_(request.POST or None)
    form_patient = form_patient_(request.POST or None)
    form_examiner = forms.ExaminerMarkSheetForm(request.POST or None)
    if request.method ==  'POST':
        station_id = request.POST.get('station')
        data_gathering_text = request.POST.getlist('data_gathering_text')     
        station = get_object_or_404(models.ThirdLevelStation,id=station_id)
        has_station = models.ExaminerMarkSheet.objects.filter(station=station).exists()
        if not has_station:
            saved_examiner_mark_sheet = save_examiner_mark_sheet(station,ExaminerMarkSheetEnum.DATA_GATHERING.value)
            save_examiner_mark_sheet_answers(data_gathering_text, saved_examiner_mark_sheet)
    
    context ={
        'form_candidate':form_candidate,
        'form_patient':form_patient,
        'form_station':form_station,
        'form_examiner':form_examiner,
        'candidate_instruction_inquiry_choices': models.CandidateInstruction.Inquiry,
        'patient_instruction_choices':models.PatientDisclosure.Disclosure
    }
    return render(request,template_name,context)


def save_examiner_mark_sheet_answers(data_gathering_text, saved_examiner_mark_sheet):
    exam_mark_sheet_answers = [models.ExaminerMarkSheetAnswer(examiner_mark_sheet = saved_examiner_mark_sheet,answer = data_gathering_text[i]) for i in range(len(data_gathering_text))]
    models.ExaminerMarkSheetAnswer.objects.bulk_create(
            exam_mark_sheet_answers
        )

def save_examiner_mark_sheet(station, heading_enum):
    saved_examiner_mark_sheet =models.ExaminerMarkSheet.objects.create(
            station=station,
            heading = heading_enum
        )

    return saved_examiner_mark_sheet

