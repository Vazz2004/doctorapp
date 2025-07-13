
from django.urls import path
from .views import  ListoDoctor , DetailDoctorView

urlpatterns = [
    path('patients',ListoDoctor.as_view()),
    path('patients/<int:pk>/',DetailDoctorView.as_view()),
]


