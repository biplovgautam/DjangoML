
from django.contrib import admin
from django.urls import path, include
from Home import views
urlpatterns = [
    path('',views.home,name="home" ),
    path('MLApp/',include("MLApp.urls") ),
    path('admin/', admin.site.urls),
]
