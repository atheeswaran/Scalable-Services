from rest_framework import serializers
from AppointmentScheduling.models import ScheduleAppointment

class AppointmentSchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleAppointment
       #using = 'Appointmentdb'
        fields='__all__'