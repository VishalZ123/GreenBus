from django.db import models

class Route(models.Model):
    source_city = models.CharField(max_length=255)
    destination_city = models.CharField(max_length=255)
    distance = models.FloatField()

    def __str__(self):
        return self.source_city + " to " + self.destination_city
    
    class Meta:
        verbose_name_plural = "Routes"

class Bus(models.Model):
    bus_name = models.CharField(max_length=255)
    total_seats = models.PositiveIntegerField()
    current_occupancy = models.PositiveIntegerField(default=0)
    available_days = models.CharField(max_length=100)  # Store days as a string
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    fare = models.FloatField()
    eta = models.TimeField(default='00:00:00')

    def __str__(self):
        return self.bus_name
    
    class Meta:
        verbose_name_plural = "Buses"
