class Elemento():
    def __init__(self,lista):
        for elemento in lista:
                print('Elemento:',elemento, 'Tipo:', type(elemento))
lista=[1452,11.23,1+2j,True, 'w3resource',(0,-1),[5,12]]