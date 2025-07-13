
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveUpdateDestroyAPIView


class ListPatientsView(ListAPIView,CreateAPIView):
    allowed_method = ['GET', 'POST']
    serializer_class= PatientSerializer
    queryset = Patient.objects.all()



class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()