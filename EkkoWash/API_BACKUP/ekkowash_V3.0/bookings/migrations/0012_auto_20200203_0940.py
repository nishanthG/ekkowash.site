# Generated by Django 2.0.7 on 2020-02-03 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='RegisteredUser',
        ),
    ]