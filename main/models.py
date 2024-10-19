import uuid
from django.db import models

# Model untuk Artikel
class Artikel(models.Model):
    judul = models.CharField(max_length=255)  # Judul artikel
    konten = models.TextField()  # Isi artikel
    tanggal_publikasi = models.DateField(auto_now_add=True)  # Tanggal publikasi otomatis saat artikel dibuat

    class Meta:
        ordering = ['-tanggal_publikasi']  # Artikel terbaru muncul pertama
 
    def __str__(self):
        return self.judul

# Model untuk Makanan
class Makanan(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama = models.CharField(max_length=255)  # Nama makanan
    deskripsi = models.TextField()  # Deskripsi singkat tentang makanan
    kategori = models.CharField(max_length=100)  # Kategori makanan (misal: "Makanan Berat", "Camilan")
    restoran = models.CharField(max_length=255)  # Nama makanan 
    harga = models.IntegerField()  # Harga makanan (tanpa pecahan)
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # Rating (contoh: 4.5)
    gambar = models.URLField(max_length=500, blank=True, null=True)  # URL untuk gambar

    class Meta:
        ordering = ['nama']  # Urutan makanan berdasarkan nama

    def __str__(self):
        return self.nama