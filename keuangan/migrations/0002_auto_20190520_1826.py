# Generated by Django 2.2 on 2019-05-20 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keuangan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keuangan',
            options={'ordering': ['tanggal'], 'verbose_name': 'Keuangan', 'verbose_name_plural': 'Keuangan'},
        ),
    ]
