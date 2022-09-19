from django.contrib import admin

from .models import Taxi, TaxiRequest


admin.site.register(Taxi)
admin.site.register(TaxiRequest)
