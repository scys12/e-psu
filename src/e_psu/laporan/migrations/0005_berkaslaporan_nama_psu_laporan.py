# Generated by Django 3.1 on 2020-09-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0004_auto_20200902_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='berkaslaporan',
            name='nama_psu_laporan',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]