def comprueba_int (n):
    while type (n) !=int or n<=0:
         n = input ("Ingresa numero entero: ")
    return n

def str_a_int (n):
    try:
        numero_ingresado = int (n)
    except:
        numero_ingresado = None
    return numero_ingresado





