# Generated by Django 3.1 on 2020-10-17 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='berkaslaporan',
            name='tanggal_proses',
            field=models.DateField(blank=True, null=True),
        ),
    ]