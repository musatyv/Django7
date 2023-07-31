from django.core.exceptions import ValidationError
import datetime

def validar_fecha_2015(fecha: datetime.date): # TODO: crear unit test para esta funcion
    if fecha.year < 2015:
        return ValidationError()