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


class AddNewPayment(forms.Form):
    cardName = forms.CharField(max_length=50)
    cardNumber = forms.CharField(max_length=50)
    expirationDate = forms.CharField(max_length=50)
    cvv = forms.CharField(max_length=3)


class AddNewNotification(forms.Form):
    message = forms.CharField(max_length=1000)


class ModifyTrain(forms.Form):
    hiddenId = forms.CharField(widget=forms.HiddenInput())
    trainNameModify = forms.CharField(max_length=100)


class DeleteTrain(forms.Form):
    trainNameDelete = forms.CharField(max_length=100)

class ModifyStation(forms.Form):
    hiddenId = forms.CharField(widget=forms.HiddenInput())
    stationNameModify = forms.CharField(max_length=100)

class DeleteStation(forms.Form):
    stationNameDelete = forms.CharField(max_length=100)

class ModifyRoute(forms.Form):
    hiddenId = forms.CharField(widget=forms.HiddenInput())
    trainNameModify = forms.CharField(max_length=100)
    startStationNameModify = forms.CharField(max_length=100)
    destinationStationNameModify = forms.CharField(max_length=100)

class DeleteRoute(forms.Form):
    routeNameDelete=forms.CharField(max_length=100)


class ModifyPlanRoute(forms.Form):
    hiddenIdModify = forms.CharField(widget=forms.HiddenInput())
    routeIdModify = forms.CharField(max_length=100)
    startTimeModify = forms.TimeField()
    arrivalTimeModify = forms.TimeField()
    dateModify = forms.DateField()
    priceModify = forms.DecimalField(max_digits=5, decimal_places=2)


class DeletePlanRoute(forms.Form):
    hiddenIdDelete = forms.CharField(widget=forms.HiddenInput())
    routeIdDelete = forms.CharField(max_length=100)
    startTimeDelete = forms.TimeField()
    arrivalTimeDelete = forms.TimeField()
    dateDelete = forms.DateField()
    priceDelete = forms.DecimalField(max_digits=5, decimal_places=2)

class AddNewBooking(forms.Form):
    hiddenId = forms.CharField(widget=forms.HiddenInput())
    userName=forms.CharField(max_length=100)
    routeName=forms.CharField(max_length=100)
    startTime = forms.CharField(max_length=100)
    arrivalTime = forms.CharField(max_length=100)
    date = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    cardName = forms.CharField(max_length=100)

class DeleteBooking(forms.Form):
    hiddenId = forms.CharField(widget=forms.HiddenInput())
    userName=forms.CharField(max_length=100)
    routeName=forms.CharField(max_length=100)
    startTime = forms.CharField(max_length=100)
    arrivalTime = forms.CharField(max_length=100)
    date = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    cardData = forms.CharField(max_length=100)


