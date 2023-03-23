# Generated by Django 4.1.7 on 2023-03-23 13:42

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('BarApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drankjes',
            name='ratio',
            field=image_cropping.fields.ImageRatioField('img', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='ratio'),
        ),
    ]