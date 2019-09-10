from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Medicines
# Create your views here.
@login_required
def create(request):
    if request.method=='POST':
        if request.POST['medicine'] and request.POST['frequency'] and request.POST['selecttime'] and request.POST['medicine_dur'] and request.POST['treat_dur'] :
            medicine=Medicines()
            medicine.medicine_name=request.POST['medicine']
            medicine.frequency=request.POST['frequency']
            medicine.select_timing= request.POST['selecttime']
            medicine.med_duration=request.POST['medicine_dur']
            medicine.treatment_duration=request.POST['treat_dur']
            medicine.patient=request.user
            medicine.save()
            return redirect('detail')
        else:
            return render(request,'create.html',{'error':'All fields are required'})
    else:
        return render(request,'create.html')
