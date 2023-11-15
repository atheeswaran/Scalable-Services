from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from displaydoctors.models import Doctor
from displaydoctors.serializers import DoctorSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status


def homePageView(request):
    return HttpResponse('Hello Patient')


def display_doctors(request):
    doctors = Doctor.objects.all()
    return render(request,"displaydoctors.html",{'doctor':doctors})


class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer

