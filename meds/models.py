from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    MEASUREMENT_CHOICES = {
        'mg': 'Milligrams',
        'gm': 'Grams',
        'ml': 'Milliliters',
        'cp': 'Cups',
    }
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    amount = models.FloatField()
    measurement = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES)

