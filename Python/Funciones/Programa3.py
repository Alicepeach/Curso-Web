import random
def adivinar():
    salida=False
    aleatorio=random.randint(1,9)
    while(salida==False):
        print("Estoy pensando en un numero del 1 al 9 cual?")
        try:
            numero=int(input())
        except:
            print("Solo numeros")
        if(numero == aleatorio):
            print("Bien adivinado")
            salida=True