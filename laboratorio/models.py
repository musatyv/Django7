from django.db import models
from .validators import validar_fecha_2015

# Create your models here.
class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=70, default=' ')
    pais = models.CharField(max_length=50, default=' ')
    class Meta:
        managed = True
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(Laboratorio,on_delete=models.CASCADE, null=True)
    especialidad = models.CharField(max_length=80, null=True)
    class Meta:
        managed = True
    
    def __str__(self):
        return self.nombre
class Producto(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    #ForeignKey me permite establecer una relacion "muchos a uno" para producto -> lab
    laboratorio = models.ForeignKey(Laboratorio,on_delete=models.CASCADE, null=True)
    f_fabricacion = models.DateField(validators=[validar_fecha_2015]) 
    p_costo = models.DecimalField(max_digits=10,decimal_places=2) 
    p_venta = models.DecimalField(max_digits=10,decimal_places=2)
    
    class Meta:
        managed = True
    
    def __str__(self):
        return self.nombre