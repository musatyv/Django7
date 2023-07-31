from django.contrib import admin
from laboratorio.models import Laboratorio,DirectorGeneral,Producto 


# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    
    
@admin.register(DirectorGeneral)
class DGAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'laboratorio',
        'f_fabricacion',
        'p_costo',
        'p_venta'
        )
    
## TODO : use the shell to make db query and take screenshots for pt2