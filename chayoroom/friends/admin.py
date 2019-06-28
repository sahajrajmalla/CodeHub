from django.contrib import admin
from .models import friends

# Register your models here.


class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(friends, FriendAdmin)
