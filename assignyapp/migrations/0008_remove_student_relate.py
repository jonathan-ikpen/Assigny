# Generated by Django 3.2.8 on 2022-09-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignyapp', '0007_auto_20220914_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='relate',
        ),
    ]
