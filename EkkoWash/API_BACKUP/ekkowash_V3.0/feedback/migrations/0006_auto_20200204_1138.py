# Generated by Django 2.0.7 on 2020-02-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20200204_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedback',
            name='picture_tag',
            field=models.CharField(choices=[('exterior', 'exterior'), ('interior', 'interior'), ('others', 'others')], default='exterior', max_length=1),
        ),
    ]
