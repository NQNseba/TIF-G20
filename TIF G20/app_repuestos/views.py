from django.shortcuts import render
from .models import Repuestos
from django.views import View 
from django.urls import reverse_lazy 

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView , UpdateView, DeleteView


class RepuestosBaseView(View):
    template_name = "repuestos.html"
    model       = Repuestos 
    fields      = "__all__"
    success_url = reverse_lazy("repuestos:all")

class RepuestosListView(RepuestosBaseView, ListView):
    ...

class RepuestosDetailView(RepuestosBaseView, DetailView): 
    template_name = "repuestos_detail_html"

class RepuestosCreateView(RepuestosBaseView, CreateView):   
    template_name = "repuestos_create_html"
    extra_context = {
        "tipo" : "Create_Repuestos"
    }

class RepuestosUpdateView(RepuestosBaseView, UpdateView):
     template_name = "repuestos_create_html"
     extra_context = {
        "tipo" : "Update_Repuestos"
    }
class RepuestosDeleteView(RepuestosBaseView, DeleteView): 
     template_name = "repuestos_create_html"
     extra_context = {
        "tipo" : "Delete_Repuestos"
    }
