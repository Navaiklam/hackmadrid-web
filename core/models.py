from django.db import models
# Si creamos algo en el modelo debemos de borrar toda la db y volver a crear con makemigrations app-name
# si no, no funcionará y dará migrations not detect
# Create your models here.
class TipoEvento(models.Model):
    typevent = models.CharField(max_length=113)

    def __str__(self):
        return self.typevent

class Event(models.Model):
    nombre = models.CharField(max_length=200)
    ponente = models.CharField(max_length=133)
    duracion = models.IntegerField()
    anio =  models.IntegerField(verbose_name='año')
    img = models.ImageField(upload_to='upload/')
    tipoevento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
