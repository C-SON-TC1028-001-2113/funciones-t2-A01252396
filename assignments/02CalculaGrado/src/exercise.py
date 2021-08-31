def calcula_grado(numero):
    if numero>=0.9 and numero <=1:
        Nota='A'
    elif numero >0.8 and numero <0.9:
        Nota='B'
    elif numero >0.7 and numero <=0.8:
        Nota='C'
    elif numero >=0.6 and numero <=0.7:
        Nota='D'
    elif numero <0.6 and numero >0:
        Nota='F'
    else:
        Nota='score incorrecto'
    return Nota
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))
if __name__=='__main__':
    main()
