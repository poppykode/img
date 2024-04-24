from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from core.decorators import role_required
from core.enums import (
    RoleEnum
)
from . import forms
from . import models
from . import utils


# Create your views here.

## stations
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def stations(request):
    template_name = 'station/stations.html'
    stations_ = models.Station.objects.all()
    return render(request,template_name,{'stations':utils.paginator(request,stations_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_station(request):
    template_name = 'station/create_station.html'
    form = forms.StationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Station successfully created.")
            return redirect('stations:stations')
    return render(request,template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_station(request, id):
    station = get_object_or_404(models.Station,id=id)
    form = forms.StationForm(request.POST or None, instance=station)
    template_name = 'station/create_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'Station {station.title} successfully updated.')
            return redirect('stations:stations')
    return render(request, template_name, {'form':form,'type':'edit','station':station})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_station(request, id):
    station = get_object_or_404(models.Station,id=id)
    template_name = 'station/delete_station.html'
    if request.method ==  'POST':
        station.delete()
        messages.success(request,f'Station {station.title} successfully deleted.')
        return redirect('stations:stations')
    return render(request, template_name, {'obj':station})

## stations categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def station_categories(request):
    template_name = 'station_category/station_categories.html'
    station_categories_ = models.StationCategory.objects.all()
    return render(request,template_name,{'station_categories':utils.paginator(request,station_categories_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_category_station(request):
    template_name = 'station_category/create_category_station.html'
    form = forms.StationCategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Station category successfully created.")
            return redirect('stations:station_categories')
    return render(request,template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_category_station(request, id):
    station_category = get_object_or_404(models.StationCategory,id=id)
    form = forms.StationCategoryForm(request.POST or None, instance=station_category)
    template_name = 'station_category/create_category_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'Category station {station_category.title} successfully updated.')
            return redirect('stations:station_categories')
    return render(request, template_name, {'form':form,'type':'edit','station_category':station_category})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_category_station(request, id):
    station_category = get_object_or_404(models.StationCategory,id=id)
    template_name = 'station_category/delete_category_station.html'
    if request.method ==  'POST':
        station_category.delete()
        messages.success(request,f'Category Station {station_category.title} successfully deleted.')
        return redirect('stations:station_categories')
    return render(request, template_name, {'obj':station_category})

## stations sub categories
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def station_sub_categories(request):
    template_name = 'station_sub_category/station_sub_categories.html'
    station_sub_categories_ = models.StationSubCategory.objects.all()
    return render(request,template_name,{'station_sub_categories':utils.paginator(request,station_sub_categories_,10)})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_category_sub_station(request):
    template_name = 'station_sub_category/create_categroy_sub_station.html'
    form = forms.StationSubCategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Sub station category successfully created.")
            return redirect('stations:sub_category_stations')
    return render(request,template_name,{'form':form})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_sub_category_station(request, id):
    station_sub_category = get_object_or_404(models.StationSubCategory,id=id)
    form = forms.StationSubCategoryForm(request.POST or None, instance=station_sub_category)
    template_name = 'station_sub_category/create_category_sub_station.html'
    if request.method ==  'POST':
        if form.is_valid():
            form.save()
            messages.success(request,f'Station sub category {station_sub_category.title} successfully updated.')
            return redirect('stations:sub_category_stations')
    return render(request, template_name, {'form':form,'type':'edit','station':station_sub_category})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def delete_sub_category_station(request, id):
    station_sub_category = get_object_or_404(models.StationSubCategory,id=id)
    template_name = 'station_sub_category/delete_sub_category_station.html'
    if request.method ==  'POST':
        station_sub_category.delete()
        messages.success(request,f'Station sub category  {station_sub_category.title} successfully deleted.')
        return redirect('stations:sub_category_stations')
    return render(request, template_name, {'obj':station_sub_category})

