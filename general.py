print("Bienvenido a la interfaz que une todas las calculadoras")
end_menu=False
while end_menu==False:
    print("Ingrese la calculadora que desea utilizar")
    print("1. Calculadora Clásica")
    print("2. Calculadora Conversora")
    print("3. Calculadora Fraccionaria")
    print("4. Salir")
    op_calc=int(input("Ingrese una opción: "))
    if op_calc==1:
        from clasica import calculadora_clasica
        calculadora_clasica()
    elif op_calc==2:
        from conversora import c_conversora
        c_conversora()
    elif op_calc==3:
        from fraccionaria import calculadora_fraccionaria
        calculadora_fraccionaria()
    elif op_calc==4:
        print("Programa finalizado")
        end_menu==True
    else:
        print("Opción incorrecta. Reintente con una de las siguientes opciones:")

x=input("Debug: Aca cierra la interfaz.")