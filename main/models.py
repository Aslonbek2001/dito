from django.db import models

class Foto(models.Model):
    name = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos')
    
    def __str__(self):
        return self.foto.name
