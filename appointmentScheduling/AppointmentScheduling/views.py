import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from AppointmentScheduling.models import ScheduleAppointment
from AppointmentScheduling.serializers import AppointmentSchedulingSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from datetime import datetime
import pika
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import datetime


""" @api_view (['POST'])
def save_appointment(request):

    patient = patient()
    patient.id = request.data['id']
    patient.name = request.data['name']
    patient.save()

    doctor = doctor()
    doctor.id = request.data['id']
    doctor.name = request.data['name']
    doctor.save()

    appointment = Schedule()
    Schedule.patient = patient
    Schedule.doctor = doctor

    appointment.save()
    return Response(status=status.HTTP_201_CREATED) """

# class AppointmentBookingView(api_view):
#     def post(self, request, format=None):
#         doctor_id = request.data.get('doctor_id')
#         appointment_time = request.data.get('appointment_time')

#         # Check if the doctor is available at the desired time
#         existing_appointments = Schedule.objects.filter(doctor_id=doctor_id, appointment_time=appointment_time)
#         if existing_appointments.exists():
#             return Response({'error': 'Doctor is not available at this time.'}, status=status.HTTP_400_BAD_REQUEST)

#         # If the doctor is available, create the appointment
#         serializer = AppointmentSchedulingSerializer(data={'doctor_id': doctor_id, 'appointment_time': appointment_time})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAppointmentView(APIView):
    def post(self, request, *args, **kwargs):
        doctor_id = request.data.get('doctor_id')
        doctor_name = request.data.get('doctor_name')
        appointment_time = request.data.get('appointment_time')
       #requested_time = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')

        # Check if the doctor is available at the requested time
        if ScheduleAppointment.objects.filter(doctor_id=doctor_id).exists():
              # Doctor is not available at the requested time
            return JsonResponse({'error': 'Doctor is not available at the requested time.'}, status=400)
        else:
              # Doctor is available, create the appointment
            ScheduleAppointment.objects.create(doctor_id=doctor_id, doctor_name=doctor_name, appointment_time=appointment_time)
            
            publish_new_appointment(ScheduleAppointment)
            return JsonResponse({'message': 'Appointment created successfully!'})
          
class AppointmentSchedulingViewSet(viewsets.ModelViewSet):
    queryset=ScheduleAppointment.objects.all()
    serializer_class=AppointmentSchedulingSerializer

def publish_new_appointment(appointment_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    appointment_instance = appointment_data.objects.latest('doctor_id')
    # Convert the datetime field to a string using DjangoJSONEncoder
    class DateTimeEncoder(DjangoJSONEncoder):
      def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super(DateTimeEncoder, self).default(obj)

    appointment_dict = model_to_dict(appointment_instance)
    message_body = json.dumps(appointment_dict, cls=DateTimeEncoder)
    channel.queue_declare(queue='new_appointment_queue')

    # Publish appointment data as a JSON message
    channel.basic_publish(exchange='',
                          routing_key='new_appointment_queue',
                          body=message_body)
    
    print(f" [x] Sent {message_body}")
    connection.close()
