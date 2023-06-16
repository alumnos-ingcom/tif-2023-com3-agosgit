def verificar(coc):
    while   coc > 9999:
        coc = int(input("Numero incorrecto, reingresar numero: "))
    return coc
def c_conversora():
    from binaria import c_bin    
    
    print("Calculadora conversora")
    print("Ingresar opcion para convertir el cambio de base")
    print("1. base binaria")
    print("2. base octal")
    coc = int(input("Ingrese el número "))
    coc = verificar(coc)
    base = int(input("opcion: "))
    if base == 1:
        
        c_bin(coc)
    if base == 2:
        from octal import c_octal
        c_octal(coc)

