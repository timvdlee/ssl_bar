# Generated by Django 4.1.7 on 2023-03-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BarApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacties',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
