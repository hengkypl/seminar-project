# Generated by Django 2.2 on 2019-05-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peserta', '0008_auto_20190520_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='hp',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='jemaat',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='nama',
            field=models.CharField(max_length=50),
        ),
    ]
