from django.urls import path
from .views import ListoDoctor, DetailDoctorView
from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet

router = DefaultRouter()
router.register('dotors', DoctorViewSet)

urlpatterns = [
    path('', ListoDoctor.as_view()),  # <- Esta es la ruta para /api/doctors/
    path('<int:pk>/', DetailDoctorView.as_view()),  # <- Esta es para /api/doctors/1/
] + router.urls
