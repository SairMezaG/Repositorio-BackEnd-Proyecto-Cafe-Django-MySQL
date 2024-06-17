from django.core.validators import RegexValidator
from django.db import models


# Modelos

class Usuario(models.Model):
    username = models.CharField(max_length=70, unique=True)
    password = models.CharField(max_length=20)  # Considerar usar un campo de contraseña adecuado más adelante.
    cedula = models.CharField(max_length=20)
    nombres_completos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message='El número de teléfono debe tener 10 dígitos')])
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    estado = models.CharField(max_length=8, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')])
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)  
    tipo_usuario = models.CharField(max_length=20, choices=[('Administrador', 'Administrador'), ('Operario', 'Operario'), ('Proveedor', 'Proveedor')])

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombres_completos


class Maquina(models.Model):
    id_maquina = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=8, choices=[('Activa', 'Activa'), ('Inactiva', 'Inactiva')], default='Activa')

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

    def __str__(self):
        return self.nombre


class Datos(models.Model):
    temperatura = models.FloatField()
    temperatura_s1 = models.FloatField()
    temperatura_s2 = models.FloatField()
    temperatura_promedio = models.FloatField()
    id_maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    fecha = models.DateField()
    

    class Meta:
        verbose_name = "Dato"
        verbose_name_plural = "Datos"

    def __str__(self):
        return self.temperatura_promedio

    


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
    



class LoteCafe(models.Model):
    numero_lote = models.IntegerField(max_length=20)
    peso = models.FloatField()
    usuario = models.CharField(max_length=50)
    nombre_proceso = models.ForeignKey(TipoProceso, on_delete=models.PROTECT)
    


    class Meta:
        verbose_name = "LoteCafe"
        verbose_name_plural = "LotesCafe"

    def __str__(self):
        return self.usuario




class Seguimiento(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=18, choices=[('Operando', 'Operando'), ('Fuera de Servicio', 'Fuera de Servicio'), ('En Mantenimiento', 'En Mantenimiento')])
    maquina = models.ForeignKey(Maquina, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    lote = models.ForeignKey(LoteCafe, on_delete=models.PROTECT)
    proceso = models.ForeignKey(TipoProceso, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Seguimiento"
        verbose_name_plural = "Seguimientos"

    def __str__(self):
        return f"{self.maquina} - {self.fecha}"
