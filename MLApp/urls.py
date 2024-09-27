from django.contrib import admin
from django.urls import path, include
from MLApp import Mviews
from ObesityApp import Oviews
from Home import views

urlpatterns = [
    path('',Mviews.mlapphome,name="mlapphome" ),
    path('ObesityApp/', Oviews.obesityhome, name='obesityhome'),
    path('ObesityApp/predict', Oviews.predictor, name='obesitypredictedresult')

]