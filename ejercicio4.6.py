# Ejercicio 6 (De 24155) 

def computepay(hours, rate):
    MAXIMO_HORAS= 40
    if (hours > MAXIMO_HORAS):
        horas_extra= hours - MAXIMO_HORAS
    else:
        horas_extra= 0
    payment= (hours*rate) + (horas_extra*(rate/2))
    return payment

try:
    hours = float(input("Ingrese el número de horas: "))
    rate = float(input("Ingrese tarifa por hora: "))
    payment = computepay(hours, rate)
    print("El pago es: ", payment)
except: 
    print("Error, favor ingresar un valor númerico")

