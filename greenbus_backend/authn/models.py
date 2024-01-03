from django.db import models
from django.contrib.auth.models import User
from buses.models import Bus

class UserProfile(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)  # Admin or User
    booked_buses = models.ManyToManyField(Bus, blank=True)

    def __str__(self):
        return self.user.username