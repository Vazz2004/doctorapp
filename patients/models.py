from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contac_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Insurance(models.Model):
    Patient = models.ForeignKey(
        Patient , related_name='insurances', on_delete=models.CASCADE
    )
    provider= models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()


class MedicalRecord(models.Model):
    Patient = models.ForeignKey(
        Patient, related_name='medical_records', on_delete=models.CASCADE
    )
    date = models.DateField()
    diagnosis = models.TextField()
    treatment= models.TextField()
    follow_up_date = models.DateField()