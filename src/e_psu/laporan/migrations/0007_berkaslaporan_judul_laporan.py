# Generated by Django 3.1 on 2020-09-14 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laporan', '0006_auto_20200914_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='berkaslaporan',
            name='judul_laporan',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]