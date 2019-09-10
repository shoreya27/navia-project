from django.shortcuts import render , get_object_or_404
from dailymedicine.models import Medicines

def home(request):

        return render(request,'home.html')


def details(request):
            medicines=Medicines.objects.filter(patient_id=request.user.id)
            print(medicines)
            return render(request,'detail.html',{'med':medicines})

def delete(request,id):
    obj=get_object_or_404(Medicines,id=id)
    if request.method=="POST":
        obj.delete()
        medicines=Medicines.objects.filter(patient_id=request.user.id)
        return  render(request,'detail.html',{'med':medicines})
