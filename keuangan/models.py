from django.db import models

ITEM_KATEGORI = (
('REGISTRASI', 'REGISTRASI'),
('IKLAN', 'IKLAN'),
('DONASI', 'DONASI'),
('LAIN2', 'LAIN2'),
('CASH', 'CASH'),
('TRANSFER', 'TRANSFER'),
)
# Create your models here.
class Keuangan(models.Model):
    tanggal = models.DateField()
    kategori = models.CharField(choices=ITEM_KATEGORI, max_length=10)
    keterangan = models.TextField(max_length=100)
    masuk = models.DecimalField(max_digits=15, decimal_places=2)
    keluar = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.keterangan

    class Meta:
        verbose_name = 'Keuangan'
        verbose_name_plural = 'Keuangan'
