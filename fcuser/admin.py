from django.contrib import admin
from .models import fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(fcuser, FcuserAdmin)
