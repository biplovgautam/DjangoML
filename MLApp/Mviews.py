from django.shortcuts import render

# Create your views here.
def mlapphome(request):
    return render(request,'MLApp/mlapp.html')

