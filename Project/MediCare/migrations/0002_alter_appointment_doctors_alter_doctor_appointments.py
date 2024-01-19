# Generated by Django 5.0 on 2023-12-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MediCare", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appointment",
            name="doctors",
            field=models.ManyToManyField(
                related_name="appointments_doc", to="MediCare.doctor"
            ),
        ),
        migrations.AlterField(
            model_name="doctor",
            name="appointments",
            field=models.ManyToManyField(
                related_name="doctors_app", to="MediCare.appointment"
            ),
        ),
    ]
