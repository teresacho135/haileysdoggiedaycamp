from django.contrib import admin
from .models import Camper, Schedule, Payment
# Register your models here.

admin.site.register(Camper)
admin.site.register(Schedule)
admin.site.register(Payment)
