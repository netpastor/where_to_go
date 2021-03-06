# Generated by Django 4.0.4 on 2022-04-14 04:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_placeimage_options_alter_placeimage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=tinymce.models.HTMLField(),
        ),
    ]
