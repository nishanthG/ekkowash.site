# Generated by Django 2.0.7 on 2020-01-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('landmark', models.TextField()),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
                ('booking_date', models.DateField()),
                ('prefered_time', models.TimeField()),
                ('alternate_time', models.TimeField()),
                ('car_type', models.TextField()),
                ('addons', models.TextField()),
                ('coupon_code', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
