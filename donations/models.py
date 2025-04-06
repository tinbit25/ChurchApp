
from django.db import models
from users.models import User

class Donation(models.Model):
    DONATION_TYPES = (
        ('one-time', 'One-time'),
        ('recurring', 'Recurring'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    donation_type = models.CharField(max_length=10, choices=DONATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)