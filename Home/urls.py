from django.contrib import admin
from django.urls import path, include
from . import views
import BaseFeatures.views as basefeatures_views

app_name = 'Home'

urlpatterns = [
    path('', views.GetHome, name="Home"),
    path('AddStation/', basefeatures_views.add_new_station),
    path('AddTrain/', basefeatures_views.add_new_train),
    path('AddRoute/', basefeatures_views.add_new_route),
    path('AddPlanRoute/', basefeatures_views.add_new_plan_route),
    path('Payment/', basefeatures_views.add_new_payment_card),
    path('Notification/', basefeatures_views.add_notification),
    path('ViewTrains/', basefeatures_views.view_trains)
]
