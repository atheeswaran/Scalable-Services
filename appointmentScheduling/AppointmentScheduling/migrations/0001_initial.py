# Generated by Django 4.2.5 on 2023-11-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField(null=True)),
                ('doctor_name', models.CharField(max_length=255, null=True)),
                ('appointment_time', models.DateTimeField(null=True)),
            ],
        ),
    ]