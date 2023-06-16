def verificar(coc):
    while   coc > 9999:
        coc = int(input("Numero incorrecto, reingresar numero: "))
    return coc
def c_conversora():
    from binaria import c_bin    
    from octal import c_octal
    from Hexa import c_hexa
    print("Calculadora conversora")
    print("Ingresar opcion para convertir el cambio de base")
    print("1. base binaria")
    print("2. base octal")
    print("3. base hexa")
    coc = int(input("Ingrese el número "))
    coc = verificar(coc)
    base = int(input("opcion: "))
    if base == 1:
        
        c_bin(coc)
    if base == 2:
        
        c_octal(coc)
    if base == 3:
        
        c_hexa(coc)

