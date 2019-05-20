from django.db import models

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
('SULSEL', 'SULSEL'),
('SULBAR', 'SULBAR'),
('SULTENG', 'SULTENG'),
('SULTRA', 'SULTRA'),
('SULUT', 'SULUT'),
('GORONTALO', 'GORONTALO'),
)

class Peserta(models.Model):
    nama = models.TextField(max_length=50)
    tgllahir = models.DateField(blank=True, null=True)
    hp = models.TextField(max_length=20)
    jemaat = models.TextField(max_length=50)
    wilayah = models.CharField(choices=ITEM_WILAYAH, max_length=10)
    tshirt = models.CharField(choices=ITEM_TSHIRT, max_length=3)
    arrivaldate = models.DateField(null = True, blank=True)
    arrivaltime = models.TimeField(null = True, blank=True)
    catatan = models.TextField()
    foto = models.ImageField(upload_to='foto/', blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = 'Peserta Seminar'
        verbose_name_plural = 'Peserta Seminar'
        ordering = ['nama']
