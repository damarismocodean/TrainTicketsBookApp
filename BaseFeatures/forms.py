from django import forms


class AddNewStation(forms.Form):
    stationName = forms.CharField(max_length=100)


class AddNewTrain(forms.Form):
    trainName = forms.CharField(max_length=100)


class AddNewRoute(forms.Form):
    trainName = forms.CharField(max_length=100)
    startStationName = forms.CharField(max_length=100)
    destinationStationName = forms.CharField(max_length=100)


class AddNewPlanRoute(forms.Form):
    routeID = forms.CharField(max_length=100)
    startTime = forms.TimeField()
    arrivalTime = forms.TimeField()
    date = forms.DateField()
    price = forms.DecimalField(max_digits=5, decimal_places=2)
