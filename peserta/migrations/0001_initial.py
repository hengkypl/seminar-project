# Generated by Django 2.2 on 2019-04-25 15:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peserta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=50)),
                ('tgllahir', models.DateField()),
                ('hp', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('jemaat', models.TextField(max_length=50)),
                ('wilayah', models.CharField(choices=[('SulSel', 'SulSel'), ('SulBar', 'SulBar'), ('SulTeng', 'SulTeng'), ('SulTra', 'SulTra'), ('SulUt', 'SulUt'), ('Gorontalo', 'Gorontalo')], max_length=10)),
                ('tshirt', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('arrivaldate', models.DateField()),
                ('arrivaltime', models.TimeField()),
                ('catatan', models.TextField()),
                ('foto', models.ImageField(upload_to='foto/')),
            ],
        ),
    ]