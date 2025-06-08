from django.contrib import admin
from .models import WalkInDrive


@admin.register(WalkInDrive)
class WalkInDriveAdmin(admin.ModelAdmin):
    list_display = ['company', 'role', 'date', 'start_time', 'end_time']
    