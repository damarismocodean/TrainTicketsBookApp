from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddNewStation, AddNewTrain, AddNewRoute, AddNewPlanRoute
from django.template import loader
from .models import Station, Train, Route, PlanRoute


# Create your views here.


def add_new_station(request):
    template = loader.get_template('AddStation.html')
    if request.method == 'POST':
        form = AddNewStation(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            station = Station()
            station.stationName = data['stationName']
            station.save()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    return HttpResponse(template.render({}, request))


def add_new_train(request):
    template = loader.get_template('AddTrain.html')
    if request.method == 'POST':
        form = AddNewTrain(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            train = Train()
            train.trainName = data['trainName']
            train.save()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    return HttpResponse(template.render({}, request))


def add_new_route(request):
    template = loader.get_template('AddRoute.html')
    if request.method == 'POST':
        form = AddNewRoute(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            route = Route()
            route.trainID = Train.objects.get(pk=data['trainName'])
            route.startStationID = Station.objects.get(pk=data['startStationName'])
            route.destinationStationID = Station.objects.get(pk=data['destinationStationName'])
            route.save()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    trains = Train.objects.all()
    stations = Station.objects.all()
    return HttpResponse(template.render({'trains': trains, 'stations': stations}, request))


def add_new_plan_route(request):
    template = loader.get_template('AddPlanRoute.html')
    if request.method == 'POST':
        form = AddNewPlanRoute(request.POST)
        if form.is_valid():
            print("valid form")
            data = form.cleaned_data
            plan_route = PlanRoute()
            plan_route.routeID = Route.objects.get(pk=data['routeID'])
            plan_route.startTime = data['startTime']
            plan_route.arrivalTime = data['arrivalTime']
            plan_route.date = data['date']
            plan_route.price = data['price']
            plan_route.save()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    routes = Route.objects.all()
    return HttpResponse(template.render({'routes': routes}, request))
