from django.contrib import admin


# Register your models here.

from .models import LeaveMessage, Subscriber

admin.site.register(Subscriber)
admin.site.register(LeaveMessage)