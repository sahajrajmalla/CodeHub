from django.contrib import admin
from .models import new_add


class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'genere')


admin.site.register(new_add, MusicAdmin)
