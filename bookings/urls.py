from django.urls import path
from .views import ListoBookings, DetailBookingsView

urlpatterns = [
    path('', ListoBookings.as_view()),  # <- Esta es la ruta para /api/doctors/
    path('<int:pk>/', DetailBookingsView.as_view()),  # <- Esta es para /api/doctors/1/
]
