# Generated by Django 2.0.7 on 2020-01-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_remove_user_booking_package_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_booking',
            name='package_type',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]