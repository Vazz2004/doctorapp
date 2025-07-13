from django.urls import path, include

urlpatterns = [
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/bookings/', include('bookings.urls')),
]
