# Generated by Django 3.2.8 on 2023-01-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignyapp', '0006_auto_20230120_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='submit_status',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Submit_Status',
        ),
    ]