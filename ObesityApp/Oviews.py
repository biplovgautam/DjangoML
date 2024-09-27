from django.shortcuts import render
from joblib import load
# Create your views here.

def obesityhome(request):
    return render(request,'ObesityApp/obesityapp.html')


model = load("./SavedModels/Obesity_Model.joblib")

def predictor(request):
    if request.method=="POST":
        age = int(request.POST.get('age'))
        gender = int(request.POST.get('gender'))
        height_cm = int(request.POST.get("height"))
        weight = int(request.POST.get("weight"))
        
        height_m = height_cm / 100
        # Calculate BMI
        bmi = weight / (height_m ** 2)
        result = model.predict([[age, gender,height_cm,weight,bmi]])
        if result[0]=="Normal Weight":
            result = "Thikka ko manxey"
        elif result[0]=="Overweight":
            result = "Hudo khado ghar ko"
        elif result[0]=="Obese":
            result = "Hudo khado ghar ko hainah khaitrai moto manxey ho"
        else:
            result = "sukey ko jiu"
        return render(request,"ObesityApp/obesityresult.html",{"result":result})
    else:
        return render(request,"ObesityApp/obesityresult.html")
    
    