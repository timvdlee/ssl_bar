# Generated by Django 4.1 on 2023-03-18 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drankjes',
            fields=[
                ('drankjes_id', models.AutoField(primary_key=True, serialize=False)),
                ('naam', models.CharField(max_length=128)),
                ('prijs', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'Drankjes',
            },
        ),
        migrations.CreateModel(
            name='Saldo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'Saldo',
            },
        ),
        migrations.CreateModel(
            name='Transacties',
            fields=[
                ('transactie_id', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('drankje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BarApp.drankjes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Transacties',
            },
        ),
        migrations.CreateModel(
            name='Stortingen',
            fields=[
                ('storting_id', models.AutoField(primary_key=True, serialize=False)),
                ('saldo_voor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('storing_amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saldo_na', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dateTime', models.DateTimeField()),
                ('done_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Executed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Stortingen',
            },
        ),
    ]
