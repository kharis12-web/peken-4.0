# Generated by Django 2.2 on 2020-11-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0005_remove_toko_gambar_ktp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toko',
            name='alamat',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='toko',
            name='nama',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='toko',
            name='nomor_ktp',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='toko',
            name='telp',
            field=models.CharField(default='', max_length=255),
        ),
    ]
