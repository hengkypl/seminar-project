# Generated by Django 2.2 on 2019-05-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keuangan', '0002_auto_20190520_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keuangan',
            name='keterangan',
            field=models.CharField(max_length=100),
        ),
    ]