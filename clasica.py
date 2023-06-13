resultado= float(input("Ingresar un numero: "))
op=str(input("Ingresar operación: "))

while op != "=":
    print(f"DEBUG: 'op' es: {op} ")
    nro= float(input("Ingresar otro numero: "))
    
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
