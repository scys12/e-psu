# Generated by Django 3.0.8 on 2020-09-22 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import serah_terima.models
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_skpd', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BerkasLaporan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_entri_laporan', models.DateField(auto_now_add=True)),
                ('nama_psu_laporan', models.CharField(max_length=100)),
                ('judul_laporan', models.CharField(max_length=100)),
                ('deskripsi_laporan', models.TextField()),
                ('foto_laporan', smartfields.fields.ImageField(blank=True, null=True, upload_to=serah_terima.models.PathAndRename('laporan/foto'))),
                ('status_laporan', models.CharField(max_length=20)),
                ('bentuk_penanganan_laporan', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_penanganan_laporan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='admin_skpd.AdminSKPD')),
                ('admin_status_laporan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='admin_skpd.AdminSKPD')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kelola_berkaslaporan',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]
