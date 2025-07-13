"""
URL configuration for doctorapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import  ListPatientsView ,DetailPatientsView , ListInsuranceView ,DetailInsuraceView ,ListMedicalRecordView, DetailMedicalRecordView

urlpatterns = [
    #url -> patients
    path('',ListPatientsView.as_view()),
    path('<int:pk>/',DetailPatientsView.as_view()),
    #url -> insurance 
    path('insurance',ListInsuranceView.as_view()),
    path('insurance/<int:pk>/',DetailInsuraceView.as_view()),
    #url -> MedicalRecord
    path('medicalrecord',ListMedicalRecordView.as_view()),
    path('medicalrecord/<int:pk>/',DetailMedicalRecordView.as_view()),
    
]


