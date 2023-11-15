from django.db import models
#from RegisterUsers.models import Patient
#from RegisterUsers.models import Doctor

# Create your models here.

class ScheduleAppointment(models.Model):
    #patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    #doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    #using = 'appointmentdb'
    doctor_id = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=255, null=True)
    appointment_time = models.DateTimeField(null=True)


