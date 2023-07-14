from django.views.generic import TemplateView
import subprocess

class RepuestosView(TemplateView):
    template_name = "index.html"
    extra_content = {
        'titulo_pagina': "Inicio"
    }
   
class CarritoView(TemplateView):
    template_name = "bloque/carrito.html"

class TarjetaView(TemplateView):
    template_name = "bloque/tarjeta.html"
