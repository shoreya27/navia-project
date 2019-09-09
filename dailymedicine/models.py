from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Medicines(models.Model):
    #medicine name
    medicine_name=models.CharField(max_length=30)
    #frequency of medicine in a day
    frequency=models.PositiveSmallIntegerField()
    #Timings
    select_timing=models.TimeField()
    #Duration of medicine
    med_duration=models.PositiveSmallIntegerField()
    #Duration of treatment
    treatment_duration=models.PositiveSmallIntegerField()
    #Foreign keying User
    patient=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.medicine_name
