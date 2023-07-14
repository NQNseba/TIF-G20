from django.contrib import admin
from django.urls import path , include

from .views import RepuestosView, CarritoView, TarjetaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RepuestosView.as_view(), name="landing_page"),
    path("repuestos/", include("app_repuestos.urls")),
    
]
