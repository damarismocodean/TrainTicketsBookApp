from django.http import HttpResponse
from django.shortcuts import render, redirect
from Home.models import Person
from .forms import AddNewStation, AddNewTrain, AddNewRoute, AddNewPlanRoute, AddNewPayment, AddNewNotification, \
    DeleteTrain, \
    ModifyTrain, DeleteStation, ModifyStation, DeleteRoute, ModifyRoute, ModifyPlanRoute, DeletePlanRoute, \
    AddNewBooking, DeleteBooking
from django.template import loader
from .models import Station, Train, Route, PlanRoute, PaymentUser, Booking, NotificationsUser


class DRoute:
    train1 = Train()
    stationS = Station()
    stationD = Station()


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


def add_new_payment_card(request):
    template = loader.get_template('Payment.html')
    if request.method == 'POST':
        form = AddNewPayment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            payment = PaymentUser()
            if request.user.is_authenticated:
                payment.userID = Person.objects.get(pk=request.user.id - 1)
                payment.cardName = data['cardName']
                payment.cardNumber = data['cardNumber']
                payment.expirationDate = data['expirationDate']
                payment.cvv = data['cvv']
                payment.save()
            else:
                print("the user is not authenticated")
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    return HttpResponse(template.render({}, request))


def add_notification(request):
    template = loader.get_template('Notification.html')
    if request.method == 'POST':
        form = AddNewNotification(request.POST)
        if form.is_valid():
            print("is valid")
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    person = Person.objects.get(pk=request.user.id - 1)
    notifications = NotificationsUser.objects.all().filter(userID=person)
    return HttpResponse(template.render({'notifications': notifications}, request))


def view_trains(request):
    template = loader.get_template('ViewTrains.html')
    if request.method == 'POST':
        if 'modify' in request.POST:
            delete_form = DeleteTrain()
            modify_form = ModifyTrain(request.POST)
            if modify_form.is_valid():
                data = modify_form.cleaned_data
                id = data['hiddenId']
                t = Train.objects.get(pk=id)
                t.trainName = data['trainNameModify']
                t.save()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
        elif 'delete' in request.POST:
            modify_form = ModifyTrain()
            delete_form = DeleteTrain(request.POST)
            if delete_form.is_valid():
                data = delete_form.cleaned_data
                t = Train.objects.get(trainName=data['trainNameDelete'])
                t.delete()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    trains = Train.objects.all()
    return HttpResponse(template.render({'trains': trains}, request))


def view_stations(request):
    template = loader.get_template('ViewStations.html')
    if request.method == 'POST':
        if 'modify' in request.POST:
            delete_form = DeleteStation()
            modify_form = ModifyStation(request.POST)
            if modify_form.is_valid():
                data = modify_form.cleaned_data
                id = data['hiddenId']
                s = Station.objects.get(pk=id)
                s.stationName = data['stationNameModify']
                s.save()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
        elif 'delete' in request.POST:
            modify_form = ModifyStation()
            delete_form = DeleteStation(request.POST)
            if delete_form.is_valid():
                data = delete_form.cleaned_data
                s = Station.objects.get(stationName=data['stationNameDelete'])
                s.delete()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    stations = Station.objects.all()
    return HttpResponse(template.render({'stations': stations}, request))


def view_routes(request):
    template = loader.get_template('ViewRoutes.html')
    if request.method == 'POST':
        if 'modify' in request.POST:
            delete_form = DeleteRoute()
            modify_form = ModifyRoute(request.POST)
            if modify_form.is_valid():
                data = modify_form.cleaned_data
                id = data['hiddenId']
                r = Route.objects.get(pk=id)
                r.trainID = Train.objects.get(pk=data['trainNameModify'])
                r.startStationID = Station.objects.get(pk=data['startStationNameModify'])
                r.destinationStationID = Station.objects.get(pk=data['destinationStationNameModify'])
                r.save()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
        elif 'delete' in request.POST:
            modify_form = ModifyRoute()
            delete_form = DeleteRoute(request.POST)
            if delete_form.is_valid():
                data = delete_form.cleaned_data
                r = Route.objects.get(pk=data['routeNameDelete'])
                r.delete()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    routes = Route.objects.all()
    trains = Train.objects.all()
    stations = Station.objects.all()
    return HttpResponse(template.render({'routes': routes, 'trains': trains, 'stations': stations}, request))


def view_plan_routes(request):
    template = loader.get_template('ViewPlanRoutes.html')
    if request.method == 'POST':
        if 'modify' in request.POST:
            delete_form = DeletePlanRoute()
            modify_form = ModifyPlanRoute(request.POST)
            if modify_form.is_valid():
                data = modify_form.cleaned_data
                id = data['hiddenIdModify']
                plan_route = PlanRoute.objects.get(pk=id)
                routeId = data['routeIdModify']
                route = Route.objects.get(pk=routeId)
                plan_route.routeID = route
                plan_route.startTime = data['startTimeModify']
                plan_route.arrivalTime = data['arrivalTimeModify']
                plan_route.date = data['dateModify']
                plan_route.price = data['priceModify']

                bookings = Booking.objects.all().filter(routeID=plan_route)
                print(plan_route.id)
                for book in bookings:
                    notification = NotificationsUser()
                    notification.userID = book.userID
                    notification.message = \
                        "A change has occur to rezervation: " \
                        + str(plan_route.routeID.route_name) \
                        + " ,start time: " + str(plan_route.startTime) \
                        + " , arrival time: " + str(plan_route.arrivalTime) \
                        + " ,date: " + str(plan_route.date) \
                        + " ,price: " + str(plan_route.price)
                    print(notification.message)
                    print(notification.userID.id)
                    notification.save()

                plan_route.save()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
        elif 'delete' in request.POST:
            modify_form = ModifyPlanRoute()
            delete_form = DeletePlanRoute(request.POST)
            if delete_form.is_valid():
                data = delete_form.cleaned_data
                id = data['hiddenIdDelete']
                plan_route = PlanRoute.objects.get(pk=id)
                second_route = plan_route

                bookings = Booking.objects.all().filter(routeID=second_route)
                print(plan_route.routeID.id)
                for book in bookings:
                    notification = NotificationsUser()
                    notification.userID = book.userID
                    notification.message = \
                        "A change has occur to rezervation:" \
                        + str(second_route.routeID.route_name) \
                        + " has been deleted"
                    print(notification.message)
                    print(notification.userID.id)
                    notification.save()

                plan_route.delete()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    plan_routes = PlanRoute.objects.all()
    routes = Route.objects.all()
    return HttpResponse(template.render({'plan_routes': plan_routes, 'routes': routes}, request))

def add_new_booking(request):
    template = loader.get_template('Booking.html')
    if request.method == 'POST':
            form = AddNewBooking(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                booking = Booking()
                if request.user.is_authenticated:
                     booking.userID = Person.objects.get(pk=request.user.id - 1)
                     id = data['hiddenId']
                     plan_route = PlanRoute.objects.get(pk=id)
                     booking.routeID = plan_route
                     print(booking.routeID.id)
                     booking.paymentID = PaymentUser.objects.get(pk=data['cardName'])
                     booking.save()
                else:
                    print("the user is not authenticated")
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    if request.user.is_authenticated:
        personA=Person.objects.get(pk=request.user.id - 1)
        payments=PaymentUser.objects.all().filter(userID=personA)
        plannedroutes=PlanRoute.objects.all()
    return HttpResponse(template.render({'personA': personA, 'payments': payments, 'routes':plannedroutes}, request))

def view_bookings(request):
    template = loader.get_template('ViewBookings.html')
    if request.method == 'POST':
        form = DeleteBooking(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            id = data['hiddenId']
            book=Booking.objects.get(pk=id)
            book.delete()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')
    if request.user.is_authenticated:
        bookings=Booking.objects.all().filter(userID=request.user.id - 1)
    return HttpResponse(template.render({'bookings' : bookings}, request))
