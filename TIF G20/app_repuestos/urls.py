from django.urls import path

from .views import  RepuestosListView,\
                    RepuestosDetailView,\
                    RepuestosCreateView,\
                    RepuestosUpdateView,\
                    RepuestosDeleteView
                   

from .router import router


app_name = "repuestos"

urlpatterns = [
  
   path("", RepuestosListView.as_view(), name = "all" ), 
   path("<int:pk>/detail/",RepuestosDetailView.as_view(), name = "detail" ),
   path("create/",RepuestosCreateView.as_view(), name = "create" ),  
   path("<int:pk>/update/",RepuestosUpdateView.as_view(), name = "update" ), 
   path("<int:pk>delete/",RepuestosDeleteView.as_view(), name = "delete" ), 
]


urlpatterns+=router.urls 