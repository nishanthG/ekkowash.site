# Generated by Django 2.0.7 on 2020-01-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_user_booking_package_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_booking',
            name='package_type',
            field=models.TextField(),
        ),
    ]