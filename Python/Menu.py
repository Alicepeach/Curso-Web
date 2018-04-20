import Funciones.Programa1
import Funciones.Programa2
import Funciones.Programa3
import Funciones.Programa4
import Funciones.Programa5
def menu():
    salir=False
    while(salir==False):
            print("Programas con funciones")
            print("1) Multiplos")
            print("2) Convertidor")
            print("3) Adivina un numero")
            print("4) Patron")
            print("5) Invertir palabra")
            print("6) Salir")
            
            opcion=int(input("Elige el programa que deseas probar"))
            if(opcion==1):
                            Funciones.Programa1.multiplos()
            elif(opcion==2):
                            Funciones.Programa2.convertir()
            elif(opcion==3):
                            Funciones.Programa3.adivinar()
            elif(opcion==4):
                            Funciones.Programa4.patron(int(input("Digite un numero"))) 
            elif(opcion==5):
                            Funciones.Programa5.invertirPalabra()  
            elif(opcion==6):
                            salir=True
       
menu()