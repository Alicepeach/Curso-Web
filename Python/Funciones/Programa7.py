class Elemento():
    def __init__(self,lista):
        for elemento in lista:
                print('Elemento:',elemento, 'Tipo:', type(elemento))
def crearObjeto():
	lista=[1452,11.23,True,'w3sorce',[5,12]]
	Elemento(lista)