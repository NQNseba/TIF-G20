from django.db import models

class Repuestos(models.Model):
    class Meta:
        db_table = "Repuestos"

    nombre = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField(blank=False,null=False) 
    abv    = models.FloatField(blank=True, null=False)

    def __str__(self):
        return f"El repuesto:{self.nombre} tiene un rating fr : {self.rating}"  
    
    
    def obtener_campos_valores(self):
        return[
            (field.verbose_name, field.value_from_object(self) )
            for field in self.__class__.meta.fields[1:]
        ]


