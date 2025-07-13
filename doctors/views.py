from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.generics import  ListAPIView, CreateAPIView , RetrieveUpdateDestroyAPIView


class ListoDoctor(ListAPIView,CreateAPIView):
    allowed_method = ['GET', 'POST']
    serializer_class= DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

