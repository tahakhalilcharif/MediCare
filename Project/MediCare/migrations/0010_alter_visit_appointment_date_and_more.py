# Generated by Django 5.0 on 2023-12-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MediCare", "0009_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visit",
            name="Appointment_Date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="visit",
            name="Consultation_Date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
