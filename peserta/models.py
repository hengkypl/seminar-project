from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

ITEM_TSHIRT = (
('XS','XS'),
('S','S'),
('M','M'),
('L','L'),
('XL','XL'),
('XXL','XXL'),
)

ITEM_WILAYAH = (
('SulSel', 'SulSel'),
('SulBar', 'SulBar'),
('SulTeng', 'SulTeng'),
('SulTra', 'SulTra'),
('SulUt', 'SulUt'),
('Gorontalo', 'Gorontalo'),
)

class Peserta(models.Model):
    nama = models.TextField(max_length=50)
    tgllahir = models.DateField()
    hp = PhoneNumberField()
    jemaat = models.TextField(max_length=50)
    wilayah = models.CharField(choices=ITEM_WILAYAH, max_length=10)
    tshirt = models.CharField(choices=ITEM_TSHIRT, max_length=3)
    arrivaldate = models.DateField()
    arrivaltime = models.TimeField()
    catatan = models.TextField()
    foto = models.ImageField(upload_to='foto/')

    def __str__(self):
        return self.nama
