# Generated by Django 3.0.8 on 2020-09-30 22:36

from django.db import migrations, models
import django.db.models.deletion
import serah_terima.models
import smartfields.fields
import smartfields.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_kelola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dokumen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', smartfields.fields.FileField(upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/video/'))),
                ('foto', smartfields.fields.ImageField(upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/foto/'))),
                ('salinan_laporan', smartfields.fields.FileField(upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/salinan_laporan/'))),
                ('status_pengelolaan_text', models.CharField(blank=True, max_length=100)),
                ('pola_pengelolaan_text', models.CharField(blank=True, max_length=100)),
                ('regulasi_pemanfaatan_psu_text', models.CharField(blank=True, max_length=100)),
                ('status_pengelolaan', smartfields.fields.FileField(blank=True, null=True, upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/status_pengelolaan/'))),
                ('pola_pengelolaan', smartfields.fields.FileField(blank=True, null=True, upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/pola_pengelolaan/'))),
                ('regulasi_pemanfaatan_psu', smartfields.fields.FileField(blank=True, null=True, upload_to=serah_terima.models.PathAndRename('serah_terima/dokumen/regulasi_pemanfaatan_psu/'))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_kelola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_kelola.AdminKelola')),
            ],
            options={
                'db_table': 'kelola_serahterima',
            },
            bases=(smartfields.models.SmartfieldsModelMixin, models.Model),
        ),
    ]
