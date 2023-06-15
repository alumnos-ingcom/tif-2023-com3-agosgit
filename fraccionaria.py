def calculadora_fraccionaria():
    #variables
    nt = 0
    dt = 0
    n2 = 0
    d2 = 0
    tot = 0
    resultado = 0

    #ingresar primer fraccion
    '''def verificar_numero(numero):
        salida = True
        try:
            int(numero)
        except:
            salida = False
        return salida'''
    nt = int(input("ingrese numerador: "))
    '''verificar_numero(nt)
    while(verificar_numero(nt) != True):
        nt = input("Numerador incorrecto, reingresar numerador: ")'''

    dt = int(input("ingrese denominador: "))

    while dt == 0:
        print("Error:El denominador no puede ser 0. Reintente.")
        dt = int(input("Introduzca denominador: "))

    #ingresar operando
    opt = str(input("ingrese el operador: "))

    #seleccionar operacion
    while opt != "=":
        n2 = int(input("ingrese numerador: "))
        '''verificar_numero(n2)
        while(verificar_numero(n2) != True):
            n2 = input("Numerador incorrecto, reingresar numerador: ")'''
        
        d2 = int(input("ingrese denominador: "))
        while d2 == 0:
            print("Error:El denominador no puede ser 0. Reintente.")
            d2 = int(input("Introduzca denominador: "))

        if opt == "+":
            nt = (nt * d2) + (n2 * dt)
            dt = dt * d2
            ans = nt, dt

        elif opt == "-":
            nt = (nt * d2) - (n2 * dt)
            dt = dt * d2
            ans = nt, dt

        elif opt == "x":
            nt = nt * n2
            dt = dt * d2
            ans = nt, dt

        elif opt == "/":
            nt = nt * d2 
            dt = n2 * dt
            ans = nt, dt
        
        else:
            print("Operación no valida, reintente con un operando válido.")
        opt = str(input("Ingresar operación: "))
    print(f"{ans}")