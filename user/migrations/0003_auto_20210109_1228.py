# Generated by Django 3.1.3 on 2021-01-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210109_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_number',
            field=models.BigIntegerField(null=True),
        ),
    ]
