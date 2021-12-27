from django import forms


class AddNewStation(forms.Form):
    stationName = forms.CharField(max_length=50)

class AddNewTrain(forms.Form):
    trainName = forms.CharField(max_length=50)

class AddNewRoute(forms.Form):
    trainName = forms.CharField(max_length=50)
    startStationName = forms.CharField(max_length=50)
    destinationStationName = forms.CharField(max_length=50)
