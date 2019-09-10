from django.shortcuts import render
from dailymedicine.models import Medicines

def home(request):

        return render(request,'home.html')


def details(request):
            medicines=Medicines.objects.filter(patient_id=request.user.id)
            print(medicines)
            return render(request,'detail.html',{'med':medicines})
