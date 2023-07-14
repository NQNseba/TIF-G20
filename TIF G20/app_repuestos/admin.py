from django.contrib import admin
from .models import Repuestos

@admin.register(Repuestos)
class RepuestosAdmin(admin.ModelAdmin):
    ... 
