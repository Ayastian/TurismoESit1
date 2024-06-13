from django.db import models

# Create your models here.
class Servicios(models.Model):
    id               = models.AutoField(db_column='Servicios', primary_key=True)
    nombre           = models.CharField(max_length=50) 
    precio           = models.IntegerField()
    descripcion      = models.CharField(max_length=200)
    foto             = models.ImageField(upload_to='servicios', null=True, blank=True)

    def __str__(self):
        return str(self.nombre)
