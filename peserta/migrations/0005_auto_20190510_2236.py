# Generated by Django 2.2 on 2019-05-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peserta', '0004_auto_20190502_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto/'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='tgllahir',
            field=models.DateField(blank=True, null=True),
        ),
    ]