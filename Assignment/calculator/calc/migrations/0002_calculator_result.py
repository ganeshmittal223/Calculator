# Generated by Django 5.0.1 on 2024-01-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='result',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
