from django.db import models

# Create your models here.

class Participante(models.Model):
    nombre = models.CharField(max_length=55)
    juego = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    contacto = models.CharField(max_length=50)
    codigo = models.CharField(max_length=35)

    class Meta:
        verbose_name = 'participante'
        verbose_name_plural = 'participantes'

    def __str__(self):
        return self.nombre + ' ' + self.juego

class Juego1(models.Model):
    codigo = models.CharField(max_length=35)
    accion = models.CharField(max_length=50)
    numero_accion = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Juego1'
        verbose_name_plural = 'Juegos1'

    def __str__(self):
        #cambiar a solo codigo 
        return self.codigo + ' / ' + str(self.creado.strftime('%d%b%y%X'))

# class ResultadosJ1(models.Model):
#     imagen = models.ImageField(upload_to='blog', null=True, blank=True)

#     def __str__(self):
#         return self.codigo + ' / ' + self.creado