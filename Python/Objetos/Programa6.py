import random
class NumerosM():
    lista=[]
    pares = 0
    impares = 0
    def __init__(self,numero=10):
        for i in range(numero):
            self.lista.append(random.randint(0,10000))
    def contar_pares_e_impares(self):
          for i in self.lista:
                if i % 2 == 0:
                      self.pares += 1
                else:
                      self.impares += 1
  