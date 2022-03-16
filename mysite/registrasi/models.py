from contextlib import nullcontext
from django.db import models
from django.utils.text import slugify

class kategori(models.Model):
    nama = models.CharField(max_length=40)
    keterangan = models.TextField(max_length=300)
    slug = models.SlugField(editable=False, blank=True, null=True)

    def save(self):
        self.slug = slugify(self.judul)
        super(kategori, self).save()

    def __str__(self):
        return self.nama

class artikel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField(max_length=1000, null=True, blank=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    kategori = models.ForeignKey(kategori, on_delete = models.SET_NULL, blank=True, null = True)
    slug = models.SlugField(editable= False, blank= True, null = True)
    gambar = models.ImageField(upload_to = 'media/', blank=True, null= True)

    def save(self):
        self.slug = slugify(self.judul)
        super(artikel, self).save()

    def __str__(self):
        return self.judul

class komen(models.Model):
    artikel = models.ForeignKey(artikel, on_delete=models.SET_NULL, blank= True, null =True)
    tanggal = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    isi = models.TextField(max_length=500, blank= True, null=True)
    email = models.EmailField(max_length=500, blank = True, null=True)
    
def __str__(self):
    return self.email