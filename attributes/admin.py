from django.contrib import admin

from attributes import models

admin.site.register(models.Beverage)
admin.site.register(models.Subscription)
admin.site.register(models.Order)
admin.site.register(models.QRCode)
