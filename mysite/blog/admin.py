from pyexpat import model
from django.contrib import admin
from . import models


class tampilartikel(admin.ModelAdmin):
    icon_name = 'description'
    list_display = ['judul', 'kategori', 'tanggal']

admin.site.register(models.artikel, tampilartikel)

class tampikategori(admin.ModelAdmin):
    list_display = ['nama', 'keterangan']

admin.site.register(models.kategori, tampikategori)

class tampikomen(admin.ModelAdmin):
    list_display = ['email', 'tanggal']

admin.site.register(models.komen, tampikomen)
