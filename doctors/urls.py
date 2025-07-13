from django.urls import path
from .views import ListoDoctor, DetailDoctorView

urlpatterns = [
    path('', ListoDoctor.as_view()),  # <- Esta es la ruta para /api/doctors/
    path('<int:pk>/', DetailDoctorView.as_view()),  # <- Esta es para /api/doctors/1/
]
