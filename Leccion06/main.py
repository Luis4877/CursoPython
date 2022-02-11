def celcius_fahrenheit(celcius):


    return celcius * (9/5 ) + 32
def farenheit_celcius(farenheit):

    return (farenheit-32) * (5/9)


dato = float(input('Inserta los grados a convertir a F:'))

print(celcius_fahrenheit(dato))

datos = float(input('Inserta los grados a convertir de Fahrenheit a Celcius:'))

print(farenheit_celcius(datos))