from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inn = models.PositiveIntegerField(unique=True)
    check = models.DecimalField(max_digits=10, decimal_places=2,
            validators=[MinValueValidator(Decimal(0.00))])

    def __str__(self):
        return self.user.username

