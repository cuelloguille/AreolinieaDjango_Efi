from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Avion, Vuelo, Pasajero, Asiento, Reserva, Boleto

admin.site.register(Avion)
admin.site.register(Vuelo)
admin.site.register(Pasajero)
admin.site.register(Asiento)
admin.site.register(Reserva)
admin.site.register(Boleto)
