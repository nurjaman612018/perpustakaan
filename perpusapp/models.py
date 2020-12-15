from django.db import models

# Create your models here.

class Kelompok(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Kelas(models.Model):
    nama = models.CharField(max_length=10)
    keterangan = models.TextField()
    
    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    jumlah = models.IntegerField()
    kelas_id = models.ForeignKey(Kelas,on_delete=models.CASCADE, null=True)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    #model.CASCADE semua data yang ada dikelompok di hapus maaka kelompok buku juga hilang
    cover = models.ImageField(upload_to='cover/',null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.judul
        