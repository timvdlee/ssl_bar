# Generated by Django 4.1 on 2023-03-18 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BarApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stortingen',
            old_name='storing_amount',
            new_name='amount',
        ),
    ]
