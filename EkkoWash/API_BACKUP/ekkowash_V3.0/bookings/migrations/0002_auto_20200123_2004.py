# Generated by Django 2.0.7 on 2020-01-23 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking_Model',
            new_name='User_Booking',
        ),
    ]
