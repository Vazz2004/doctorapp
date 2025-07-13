from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.generics import  ListAPIView, CreateAPIView , RetrieveUpdateDestroyAPIView


class ListoBookings(ListAPIView,CreateAPIView):
    '''
    Obtiente la lista de de citas programadas 
    '''
    allowed_method = ['GET', 'POST']
    serializer_class= AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailBookingsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

