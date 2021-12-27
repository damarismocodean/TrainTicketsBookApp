from django.db import models

# Create your models here.
class Train(models.Model):
    trainNumber=models.CharField(primary_key=True,max_length=50)
    trainName=models.CharField(max_length=50)
    def __str__(self):
        return self.trainNumber

class Route(models.Model):
    routeID=models.CharField(primary_key=True,max_length=50)
    trainNumber = models.ForeignKey('Train',on_delete=models.CASCADE)
    startStationID = models.ForeignKey('Station', on_delete=models.CASCADE)
    destinationStation=models.ForeignKey('Station',on_delete=models.CASCADE)
    def __str__(self):
        return self.routeID

class Station(models.Model):
    stationID=models.CharField(primary_key=True,max_length=50)
    stationName=models.CharField(max_length=50)
    def __str__(self):
        return self.stationID

class PlanRoute(models.Model):
    planRouteID=models.CharField(primary_key=True,max_length=50)
    routeID=models.ForeignKey('Route',on_delete=models.CASCADE)
    startTime=models.CharField(max_length=50)
    arrivalTime=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
