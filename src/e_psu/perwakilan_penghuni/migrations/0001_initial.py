# Generated by Django 3.1 on 2020-08-29 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerwakilanPenghuni',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.account')),
                ('nama', models.CharField(max_length=30)),
                ('alamat_rumah', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'kelola_perwakilanpenghuni',
            },
        ),
    ]
