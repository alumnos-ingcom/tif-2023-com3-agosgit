def c_octal(coc):
    coc = 0
    resto = 0

    while coc >= 8:
        resto = coc % 8
        coc = coc // 8
        resultado = str(resto) + resultado 
    resultado = str(coc) + resultado 
    print(f"{resultado}")