def str_hexa(valor):
    if(valor<10):
        sal = str(valor)
    elif(valor == 10):
        sal = "A"
    elif(valor == 11):
        sal = "B"
    elif(valor == 12):
        sal = "C"
    elif(valor == 13):
        sal = "D"
    elif(valor == 14):
        sal = "E"
    elif(valor == 15):
        sal = "F"
    return sal