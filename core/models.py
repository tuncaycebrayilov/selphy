from django.db import models

# Create your models here.
from mysite.utils.base import BaseModel

class Subscriber(BaseModel):
    email = models.EmailField(verbose_name='Email Address')

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email

    
class LeaveMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name