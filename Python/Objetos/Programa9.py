class Numero():
    factorial=[]
    numero=0
    total=1
    def __init__(self,numero):
        tmp=[]
        self.numero=numero
        for i in range(numero):
            if numero != 0 or numero != 1:
                tmp.append(i+1)
        self.factorial=tmp
    def encontrarFactorial(self):
        for j in (self.factorial):
            self.total*=j
        return "El factorial de: "+str(self.numero) +" es "+ str(self.total)