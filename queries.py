import django
django.setup()

from laboratorio.models import Laboratorio, DirectorGeneral, Producto  # noqa: E402
# Obtener los objetos de Laboratorio, Director General y Producto
lab = Laboratorio.objects.all()

director = DirectorGeneral.objects.all()

productos =  Producto.objects.all()

# Obtener el producto cuyo nombre es 'Producto1'
p1 = Producto.objects.get(nombre='Producto1')
print(p1)
# Obtener el laboratorio de Producto1
p1_lab = p1.laboratorio

print(f'--Nombre lab de Producto1: \n {p1_lab.nombre} \n') 

# Obtener todos los productos ordenados por su nombre
productos_ordenados = productos.order_by('nombre')

for p in productos_ordenados:   
    # Realice una consulta por pantalla que imprima los laboratorios de todos los productos
    print(f"nombre -> {p.nombre} | Laboratorio -> {p.laboratorio.nombre}")

