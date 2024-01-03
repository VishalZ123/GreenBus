from django.db import models
from authn.models import UserProfile
from buses.models import Bus

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)  # Booked, Cancelled, etc.

    def __str__(self):
        return self.user.user.username + " booked " + self.bus.bus_name + " on " + str(self.booking_date)

    class Meta:
        verbose_name_plural = "Bookings"
