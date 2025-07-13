from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('docs.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/bookings/', include('bookings.urls')),

]
