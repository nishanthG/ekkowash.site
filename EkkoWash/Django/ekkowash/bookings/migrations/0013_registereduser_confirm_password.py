# Generated by Django 2.0.7 on 2020-02-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_auto_20200203_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='confirm_password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
