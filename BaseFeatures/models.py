from __future__ import annotations
from django.db import models
from abc import ABC, abstractmethod
from random import randrange
from typing import List


"""Patern Observer Implmented"""
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class PersonConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0:
            message = "A chage has occur!!!"

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class RouteConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        self._state = randrange(0, 10)
        self.notify()



# Create your models here.
class Train(models.Model):
    trainName = models.CharField(max_length=100)
    def __str__(self):
        return self.trainName

class Route(models.Model):
    trainID = models.ForeignKey('Train',on_delete=models.CASCADE)
    startStationID = models.ForeignKey('Station', related_name="startStation", on_delete=models.CASCADE)
    destinationStationID = models.ForeignKey('Station', related_name="destinationStation", on_delete=models.CASCADE)

    @property
    def route_name(self):
        return '%s-%s-%s' % (self.trainID,self.startStationID, self.destinationStationID)

class Station(models.Model):
    stationName = models.CharField(max_length=100)

    def __str__(self):
        return self.stationName

class PlanRoute(models.Model):

    routeID = models.ForeignKey('Route', on_delete=models.CASCADE)
    startTime = models.CharField(max_length=100)
    arrivalTime = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Booking(models.Model):
    userID = models.ForeignKey('Home.Person', on_delete=models.CASCADE)
    routeID = models.ForeignKey('PlanRoute', on_delete=models.CASCADE)
    paymentID = models.ForeignKey('PaymentUser', on_delete=models.CASCADE)

class PaymentUser(models.Model):
    userID = models.ForeignKey('Home.Person', on_delete=models.CASCADE)
    cardName = models.CharField(max_length=100)
    cardNumber = models.CharField(max_length=100)
    expirationDate = models.CharField(max_length=100)
    cvv = models.CharField(max_length=3)

class NotificationsUser(models.Model):
    userID = models.ForeignKey('Home.Person',on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
