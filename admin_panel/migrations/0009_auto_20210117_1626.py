# Generated by Django 3.1.3 on 2021-01-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_auto_20210117_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
