from django.contrib import admin
from .models import country, customer

# Register your models here.


class countryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country')


class customerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password',
                    'order', 'country', 'date')


admin.site.register(country, countryAdmin)
admin.site.register(customer, customerAdmin)
