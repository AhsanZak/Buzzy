# Generated by Django 3.1.3 on 2021-01-17 07:51

from django.db import migrations
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_imagedetail_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetail',
            name='image',
            field=thumbnails.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
