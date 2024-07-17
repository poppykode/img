from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.decorators import role_required, subscription_required
from core.enums import RoleEnum
from . import forms
from . import models
from . import utils
from core.utils import paginator


# Create your views here.


## stations
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def first_level_stations(request):
    template_name = "first_level_station/first_level_stations.html"
    first_level_stations_ = models.FirstLevelStation.objects.all()
    return render(
        request,
        template_name,
        {"items": paginator(request, first_level_stations_, 10)},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_first_level_station(request):
    template_name = "first_level_station/create_first_level_station.html"
    form = forms.FirstLevelStationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "First level station successfully created.")
            return redirect("stations:first_level_stations")
    return render(request, template_name, {"form": form, "type": "create"})


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_first_level_station(request, id):
    first_level_station_ = get_object_or_404(models.FirstLevelStation, id=id)
    form = forms.FirstLevelStationForm(
        request.POST or None, instance=first_level_station_
    )
    template_name = "first_level_station/create_first_level_station.html"
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"First level station {first_level_station_.title} successfully updated.",
            )
            return redirect("stations:first_level_stations")
    return render(
        request,
        template_name,
        {"form": form, "type": "edit", "obj": first_level_station_},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_first_level_station(request, id):
    first_level_station = get_object_or_404(models.FirstLevelStation, id=id)
    template_name = "first_level_station/delete_first_level_station.html"
    if request.method == "POST":
        first_level_station.delete()
        messages.success(
            request,
            f"First level station {first_level_station.title} successfully deleted.",
        )
        return redirect("stations:first_level_stations")
    return render(request, template_name, {"obj": first_level_station})


## stations categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def second_level_stations(request):
    template_name = "second_level_station/second_level_stations.html"
    second_level_stations_ = models.SecondLevelStation.objects.all()
    return render(
        request,
        template_name,
        {"items": paginator(request, second_level_stations_, 10)},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_second_level_station(request):
    template_name = "second_level_station/create_second_level_station.html"
    form = forms.SecondLevelStationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Second level station successfully created.")
            return redirect("stations:second_level_stations")
    return render(request, template_name, {"form": form, "type": "create"})


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_second_level_station(request, id):
    second_level_station = get_object_or_404(models.SecondLevelStation, id=id)
    form = forms.SecondLevelStationForm(
        request.POST or None, instance=second_level_station
    )
    template_name = "second_level_station/create_second_level_station.html"
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Second level station {second_level_station.title} successfully updated.",
            )
            return redirect("stations:second_level_stations")
    return render(
        request,
        template_name,
        {"form": form, "type": "edit", "obj": second_level_station},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_second_level_station(request, id):
    second_level_station = get_object_or_404(models.SecondLevelStation, id=id)
    template_name = "second_level_station/delete_second_level_station.html"
    if request.method == "POST":
        second_level_station.delete()
        messages.success(
            request,
            f"Second level station {second_level_station.title} successfully deleted.",
        )
        return redirect("stations:second_level_stations")
    return render(request, template_name, {"obj": second_level_station})


## stations sub categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def third_level_stations(request):
    template_name = "third_level_station/third_level_stations.html"
    third_level_stations_ = models.ThirdLevelStation.objects.all()
    return render(
        request,
        template_name,
        {"items": paginator(request, third_level_stations_, 10)},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_third_level_station(request):
    template_name = "third_level_station/create_third_level_station.html"
    form = forms.ThirdLevelStationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Second level station successfully created.")
            return redirect("stations:third_level_stations")
    return render(request, template_name, {"form": form, "type": "create"})


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_third_level_station(request, id):
    third_level_station = get_object_or_404(models.ThirdLevelStation, id=id)
    form = forms.ThirdLevelStationForm(
        request.POST or None, instance=third_level_station
    )
    template_name = "third_level_station/create_third_level_station.html"
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Second level station {third_level_station.title} successfully updated.",
            )
            return redirect("stations:third_level_stations")
    return render(
        request,
        template_name,
        {"form": form, "type": "edit", "obj": third_level_station},
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_third_level_station(request, id):
    third_level_station = get_object_or_404(models.ThirdLevelStation, id=id)
    template_name = "third_level_station/delete_third_level_station.html"
    if request.method == "POST":
        third_level_station.delete()
        messages.success(
            request,
            f"Second level station  {third_level_station.title} successfully deleted.",
        )
        return redirect("stations:third_level_stations")
    return render(request, template_name, {"obj": third_level_station})


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def station_creator(request):
    template_name = "station_creator.html"
    if request.method == "POST":
        # Station Details
        station = get_object_or_404(
            models.ThirdLevelStation, id=request.POST.get("station")
        )
        station_exists = models.ExaminerMarkSheet.objects.filter(station=station).exists()
        if not station_exists:
            utils.save_instruction_bulk(
                station,
                request.POST.getlist("candidate_instruction_heading"),
                request.POST.getlist("candidate_instruction_text"),
                request.POST.getlist("patient_instruction_heading"),
                request.POST.getlist("patient_instruction_text"),
            )
            # Examiner Mark Sheet
            # has_station = models.ExaminerMarkSheet.objects.filter(station=station).exists()
            utils.save_mark_sheet_bulk(
                station,
                request.POST.getlist("data_gathering_text"),
                request.POST.getlist("management_text"),
                request.POST.getlist("interpersonal_skills_text"),
            )
            # station Approach
            utils.save_station_approach(
                station,
                request.POST.get("station_approach_learning_points"),
                request.POST.getlist("station_approach_link"),
            )
            messages.success(request,f"Sation {station.title} was successfully created.")
        else:
            messages.error(request,f"Sation {station.title} already exists.")
        return redirect('stations:stations')
    context = {
        "stations": utils.get_all_stations(),
        "candidate_instruction_inquiry_choices": models.CandidateInstruction.Inquiry,
        "patient_instruction_disclosure_choices": models.PatientInstruction.Disclosure,
    }
    return render(request, template_name, context)

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def stations_admin(request):
    template_name = "station/stations.html"
    station_ = models.FirstLevelStation.objects.all()
    return render(
        request,
        template_name,
        {"items": paginator(request, station_, 10)}
    )

#User views
@subscription_required
@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def first_level_station_view(request):
    template_name = "first_level_station/first_level_station_view.html"
    station_ = models.FirstLevelStation.objects.all()
    return render(
        request,
        template_name,
        {"items": paginator(request, station_, 10)}
    )

@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def second_level_station_view(request,id):
    template_name = "second_level_station/second_level_station_view.html"
    first_level_station_ = get_object_or_404(models.FirstLevelStation , id = id)
    station_ = models.SecondLevelStation.objects.filter(first_level_station= first_level_station_)
    return render(
        request,
        template_name,
        {"items": paginator(request, station_, 10),'obj':first_level_station_}
    )

@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def third_level_station_view(request,id):
    template_name = "third_level_station/third_level_station_view.html"
    second_level_station_ = get_object_or_404(models.SecondLevelStation , id = id)
    station_ = models.ThirdLevelStation.objects.filter(second_level_station= second_level_station_)
    return render(
        request,
        template_name,
        {"items": paginator(request, station_, 10),'obj':second_level_station_}
    )

@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def stations_menu_view(request, id,title):
    template_name = "station/stations_menu_view.html"
    return render(
        request,
        template_name,
        {'id':id,'title':title}
    )


@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def station_practice(request, id, type):
    template = ['candidate_instructions.html','patient_instruction.html','examiner_mark_sheet.html' ,'station_approach.html']
    template_name = ""
    if type == 'candidate_instructions':
        template_name = f'station/{template[0]}'
    elif type == 'patient_instruction':
        template_name = f'station/{template[1]}'
    elif type == 'examiner_mark_sheet':
        template_name = f'station/{template[2]}'
    else:
        template_name = f'station/{template[3]}'

    obj = get_object_or_404(models.ThirdLevelStation, id = id)
    return render(
        request,
        template_name,
        {'obj':obj,'type':type}
    )






