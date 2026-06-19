from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    departure_country = models.CharField(max_length=100)
    arrival_country = models.CharField(max_length=100)
    flight_status = models.CharField(max_length=50)

    def __str__(self):
        return self.flight_number
