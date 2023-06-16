def c_bin(coc):
    #coc = 0
    resto = 0
    resultado = ""

    #coc = int(input("Ingrese el número "))
    #from conversorag import verificar
    #verificar(coc)

    while coc >= 2:
        resto = coc % 2
        coc = coc // 2
        resultado = str(resto) + resultado 
    resultado = str(coc) + resultado 
    print(f"{resultado}")