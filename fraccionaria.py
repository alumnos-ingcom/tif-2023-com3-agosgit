def recibir_fraccion():
    num=float(input("Introduzca numerador: "))
    den=float(input("Introduzca denominador: "))
    while den==0:
        print("Error:El denominador no puede ser 0. Reintente.")
        den=float(input("Introduzca denominador: "))
    
    return num/den

def show_menu():
    print("Ingrese la operación que desea realizar")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")


print("Bienvenido a la calculadora fraccionaria")
resultado=recibir_fraccion()

op=str(input("Ingresar operación: "))

while op != "=":
    print("Ingrese el siguiente operando")
    nro= recibir_fraccion()
    
    if op== "+":
        resultado+= nro
    elif op=="-":
        resultado-= nro
    elif op=="*":
        resultado*= nro
    elif op== "/":
        if nro!=0:
            resultado/= nro
        else:
            print(f"Operacion no realizada. El divisor no puede ser 0.")
    else:
        print("Operación no valida, reintente con un operando válido.")
    op=str(input("Ingresar operación: "))

print(f"{resultado}")
x=input("Presione enter para salir")