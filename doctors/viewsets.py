from rest_framework import viewsets
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.decorators import action

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class= DoctorSerializer
    queryset = Doctor.objects.all()
    
    @action(["POST"],detail=True)
    def toggle_vacation(self,request,pk):
       doctor = self.get_object()
       if doctor.is_on_vacation:
           doctor
