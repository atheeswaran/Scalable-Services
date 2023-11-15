"""
URL configuration for Healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#from RegisterUsers.views import homePageView
#from RegisterUsers.views import display_patients, display_doctors
from AppointmentScheduling.views import BookAppointmentView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    # path('',homePageView, name='home'),
    # path('displaypatients/',display_patients, name ='display patients'),
    # path('displaydoctors/',display_doctors, name ='display doctors'),

    #path('admin/', admin.site.urls),
    #path('RegisterUsers/',include('RegisterUsers.urls')),
    #path("flightServices/findFlights/",views.find_flights),
    path('api/book-appointment/', BookAppointmentView.as_view(), name='book-appointment'),
    #path('receive-rabbitmq-message/', receive_rabbitmq_message, name='receive_rabbitmq_message'),
    #path('', include(router.urls)),
]

