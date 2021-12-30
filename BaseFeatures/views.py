from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Home.models import Person
from .forms import AddNewStation, AddNewTrain, AddNewRoute, AddNewPlanRoute, AddNewPayment, AddNewNotification, \
    DeleteTrain, \
    ModifyTrain, DeleteStation, ModifyStation, DeleteRoute, ModifyRoute, ModifyPlanRoute, DeletePlanRoute, \
    AddNewBooking, DeleteBooking, DeleteUser, ModifyDataUser, SearchRoute
from django.template import loader

from .iterator import DatabaseCollection
from .models import Station, Train, Route, PlanRoute, PaymentUser, Booking, NotificationsUser
from datetime import date, datetime

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
    routes = Route.objects.all()

    dc = DatabaseCollection(list(PlanRoute.objects.all()))
    reversed_plan_routes = []
    for i in dc:
        reversed_plan_routes.append(i)
    return HttpResponse(template.render({'plan_routes': reversed_plan_routes, 'routes': routes}, request))


def add_new_booking(request):
    template = loader.get_template('Booking.html')
    search = False
    if request.method == 'POST':
        if 'reserve' in request.POST:
            form_search = SearchRoute()
            form_booking = AddNewBooking(request.POST)
            if form_booking.is_valid():
                data = form_booking.cleaned_data
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
        elif 'search' in request.POST:
            form_booking = AddNewBooking()
            form_search = SearchRoute(request.POST)
            if form_search.is_valid():
                data = form_search.cleaned_data
                s1Id = data['startStationID']
                s2Id = data['destinationStationID']
                date = data['dateSearch']
                routes = Route.objects.all().filter(startStationID=s1Id,destinationStationID=s2Id)
                routesIds = []
                for r in routes:
                    routesIds.append(r.id)
                searchPlanedRoutes = PlanRoute.objects.all().filter(routeID=tuple(routesIds), date=date)
                search = True
            else:
                return HttpResponse('<h1>Invalid form</h1>')
    if request.user.is_authenticated:
        stations = Station.objects.all()
        personA = Person.objects.get(pk=request.user.id - 1)
        payments = PaymentUser.objects.all().filter(userID=personA)
        if search:
            planedroutes = searchPlanedRoutes
        else:
            planedroutes = PlanRoute.objects.all()
    return HttpResponse(template.render({'personA': personA, 'payments': payments, 'routes': planedroutes, 'stations': stations}, request))


def view_bookings(request):
    template = loader.get_template('ViewBookings.html')
    if request.method == 'POST':
        form = DeleteBooking(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            id = data['hiddenId']
            book = Booking.objects.get(pk=id)
            plan_route = PlanRoute.objects.all().get(pk=book.routeID.id)
            print(plan_route.date)
            today = date.today()
            date_reservation = datetime.strptime(plan_route.date, '%Y-%m-%d').date()
            print((date_reservation - today).days)
            if (date_reservation-today).days < 2:
                return HttpResponse('<h1>Can not cancel this reservation. Too late</h1>')
            book.delete()
        else:
            return HttpResponse('<h1>Invalid Data</h1>')

    if request.user.is_authenticated:
        bookings = Booking.objects.all().filter(userID=request.user.id - 1)
    return HttpResponse(template.render({'bookings': bookings}, request))


def view_users(request):
    template = loader.get_template('ViewUsers.html')
    if request.method == 'POST':
        if 'modify' in request.POST:
            delete_form = DeleteUser()
            modify_form = ModifyDataUser(request.POST)
            if modify_form.is_valid():
                data = modify_form.cleaned_data
                id = data['hiddenId']
                p = Person.objects.get(pk=id)
                u = User.objects.get(username=p.username)
                u.username = data['usernameModify']
                u.set_password(data['passwordModify'])
                u.save()
                p.name = data['nameModify']
                p.username = data['usernameModify']
                p.password = data['passwordModify']
                p.email = data['emailModify']
                p.number = data['numberModify']
                p.save()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
        elif 'delete' in request.POST:
            modify_form = ModifyDataUser()
            delete_form = DeleteUser(request.POST)
            if delete_form.is_valid():
                data = delete_form.cleaned_data
                p = Person.objects.get(username=data['usernameDelete'])
                u = User.objects.get(username=data['usernameDelete'])
                [s.delete() for s in Session.objects.all() if s.get_decoded().get('_auth_user_id') == u.id]
                u.is_active = False
                u.save()
                u.delete()
                p.delete()
            else:
                return HttpResponse('<h1>Invalid Data</h1>')
    users = Person.objects.all()
    return HttpResponse(template.render({'users': users}, request))


def logout(request):
    auth.logout(request)
    return redirect("http://127.0.0.1:8000/")
