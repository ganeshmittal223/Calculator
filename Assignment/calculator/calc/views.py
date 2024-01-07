# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CalculatorForm

# views.py
from django.shortcuts import render
from .forms import CalculatorForm

def calculate(request):
    result = None  # Initialize result to None

    if request.method == 'POST':
        form = CalculatorForm(request.POST)

        if form.is_valid():
            operand1 = form.cleaned_data['operand1']
            operator = form.cleaned_data['operator']
            operand2 = form.cleaned_data['operand2']

            result = perform_calculation(operand1, operator, operand2)

    else:
        form = CalculatorForm()

    return render(request, 'index.html', {'form': form, 'result': result})


def perform_calculation(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            return operand1 / operand2
        else:
            return 'Cannot divide by zero'

    return 'Invalid operator'
