# Generated by Django 3.0.8 on 2020-09-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berkaslaporan',
            name='status_laporan',
            field=models.CharField(choices=[('BELUM', 'Belum Diproses'), ('SEDANG', 'Sedang Diproses'), ('SUDAH', 'SUDAH Diproses')], max_length=6),
        ),
    ]