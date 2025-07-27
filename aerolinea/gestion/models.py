from django.db import models

# Create your models here.
from django.db import models

class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    filas = models.IntegerField()
    columnas = models.IntegerField()

    def __str__(self):
        return self.modelo

class Vuelo(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.DurationField()
    estado = models.CharField(max_length=50)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origen} a {self.destino}"

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    tipo_documento = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.documento})"

class Asiento(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    numero = models.CharField(max_length=5)
    fila = models.IntegerField()
    columna = models.IntegerField()
    tipo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Asiento {self.numero}"

class Reserva(models.Model):
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    asiento = models.OneToOneField(Asiento, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_reserva = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Reserva {self.codigo_reserva}"

class Boleto(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE)
    codigo_barra = models.CharField(max_length=50)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return f"Boleto de {self.reserva.pasajero.nombre}"
