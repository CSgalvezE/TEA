#Parte 2 de Iteración 

total= 0
counter= 0
while True: 
    try: 
        input_str = input("Ingrese un número: ")
        if(input_str == "done"): 
            break 
        else: 
            total = total + input(input_str)
            counter= counter + 1 
            average = total / counter 
    except:
            print("Valor no es valido")
            continue 
print("Total: ", total)
print("Contador: ", counter)
print("Promedio: ", average)