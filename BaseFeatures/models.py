from django.db import models


# Create your models here.
class Train(models.Model):
    trainName = models.CharField(max_length=100)


class Route(models.Model):
    trainID = models.ForeignKey('Train', on_delete=models.CASCADE)
    startStationID = models.ForeignKey('Station', related_name="startStation", on_delete=models.CASCADE)
    destinationStationID = models.ForeignKey('Station', related_name="destinationStation", on_delete=models.CASCADE)


class Station(models.Model):
    stationName = models.CharField(max_length=100)


class PlanRoute(models.Model):
    routeID = models.ForeignKey('Route', on_delete=models.CASCADE)
    startTime = models.CharField(max_length=100)
    arrivalTime = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)

