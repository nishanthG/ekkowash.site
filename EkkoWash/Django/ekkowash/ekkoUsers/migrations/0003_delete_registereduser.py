# Generated by Django 2.0.7 on 2020-02-11 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ekkoUsers', '0002_remove_registereduser_confirm_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegisteredUser',
        ),
    ]
