from django.db import models
from django.contrib.auth.models import User


# Create your models here.
PET_TYPES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat')

    )
class Pet(models.Model):
    type=models.CharField(max_length=50,choices=PET_TYPES)
    name=models.CharField(max_length=100)
    birthday=models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "pets"

    def __str__(self):
        return self.name