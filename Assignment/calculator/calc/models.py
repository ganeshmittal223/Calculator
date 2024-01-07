# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Calculator(models.Model):
    operand1 = models.FloatField()
    operator = models.CharField(max_length=1)
    operand2 = models.FloatField()
    result = models.FloatField()

    def perform_calculation(self):
        if self.operator == '+':
            return self.operand1 + self.operand2
        elif self.operator == '-':
            return self.operand1 - self.operand2
        elif self.operator == '*':
            return self.operand1 * self.operand2
        elif self.operator == '/':
            if self.operand2 != 0:
                return self.operand1 / self.operand2
            else:
                raise ValueError('Cannot divide by zero')

        raise ValueError('Invalid operator')

    def __str__(self):
        return f"{self.operand1} {self.operator} {self.operand2} = {self.result}"

@receiver(post_save, sender=Calculator)
def create_calculator_instance(sender, instance, created, **kwargs):
    if created:
        Calculator.objects.create(
            operand1=instance.operand1,
            operator=instance.operator,
            operand2=instance.operand2,
            result=instance.perform_calculation()
        )
