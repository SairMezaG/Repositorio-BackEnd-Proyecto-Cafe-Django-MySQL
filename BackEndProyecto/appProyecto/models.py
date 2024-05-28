""" from django.core.validators import RegexValidator """
from django.db import models

# Create your models here.

class LoteCafe(models.Model):
    peso = models.FloatField()  
    proveedor = models.CharField(max_length=50)
    tipo_proceso = models.CharField(max_length=50)
    variedad_cafe = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo_proceso
    
    



    
estadosOperario =[
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
    
]         


class Operario(models.Model):
    cedula = models.CharField(max_length=20)
    nombres_completos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "Operario"
        verbose_name_plural = "Operarios"

    def __str__(self):
        return self.nombres_completos






estadosMaquina =[
    ('Activa', 'Activa'),
    ('Inactiva', 'Inactiva'),
    
]         


class Maquina(models.Model):
   
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Maquina"
        verbose_name_plural = "Maquinas"

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    cedula = models.CharField(max_length=20)
    nombres_completos = models.CharField(max_length=50)
    telefono = models.CharField(  max_length=10 )
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombres_completos
    
    
    
estadosSeguimiento =[
    ('Encendido', 'Encendido'),
    ('Apagado', 'Apagado'),
    ('Mantenimiento', 'Mantenimiento')
]     


class Seguimiento(models.Model):
    fecha = models.DateField()  # Use DateField for dates
    estado = models.BooleanField(default=True)
    rotor = models.CharField(max_length=10)
    temperatura_s1 = models.FloatField()
    temperatura_s2 = models.FloatField()
    temperatura_promedio = models.FloatField()
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    lote_cafe = models.ForeignKey(LoteCafe, on_delete=models.PROTECT)
    operario = models.ForeignKey(Operario, on_delete=models.PROTECT)
    ventilador = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Seguimiento"
        verbose_name_plural = "Seguimientos"

    def __str__(self):
        return f"{self.maquina} - {self.fecha}"


class TipoProceso(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de Proceso"
        verbose_name_plural = "Tipos de Procesos"

    def __str__(self):
        return self.nombre


class Variedad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Variedad"
        verbose_name_plural = "Variedades"

    def __str__(self):
        return self.nombre

    