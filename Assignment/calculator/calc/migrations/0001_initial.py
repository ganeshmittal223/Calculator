# Generated by Django 5.0.1 on 2024-01-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operand1', models.FloatField()),
                ('operator', models.CharField(max_length=1)),
                ('operand2', models.FloatField()),
            ],
        ),
    ]
