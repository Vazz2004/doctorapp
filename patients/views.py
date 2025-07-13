
from .models import Patient , Insurance ,MedicalRecord
from .serializers import PatientSerializer , InsuranceSerializer , MedicalRecordSerializer
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveUpdateDestroyAPIView


class ListPatientsView(ListAPIView,CreateAPIView):
    allowed_method = ['GET', 'POST']
    serializer_class= PatientSerializer
    queryset = Patient.objects.all()



class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ListInsuranceView(ListAPIView,CreateAPIView):
    allowed_method = ['GET', 'POST']
    serializer_class= InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuraceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListAPIView,CreateAPIView):
    allowed_method = ['GET', 'POST']
    serializer_class= MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
