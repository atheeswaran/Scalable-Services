from rest_framework import serializers
from displaydoctors.models import Doctor

# class PatientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Patient        
#         using = 'Registerusersdb'
#         fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor       
        #using = 'RegisterUsersdb'
        fields='__all__'