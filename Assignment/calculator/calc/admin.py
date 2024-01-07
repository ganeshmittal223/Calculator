# admin.py
from django.contrib import admin
from .models import Calculator

class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('operand1', 'operator', 'operand2', 'result')
    search_fields = ('operand1', 'operand2', 'operator')  # Add fields for search functionality

admin.site.register(Calculator, CalculatorAdmin)
