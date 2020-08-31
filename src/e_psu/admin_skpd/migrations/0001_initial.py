# Generated by Django 3.0.8 on 2020-08-28 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSKPD',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nama', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'kelola_adminskpd',
            },
        ),
    ]