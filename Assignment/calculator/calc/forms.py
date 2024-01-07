# forms.py
from django import forms
from .models import Calculator

class CalculatorForm(forms.ModelForm):
    class Meta:
        model = Calculator
        fields = ['operand1', 'operator', 'operand2']
