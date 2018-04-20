import Objetos.Programa6
import Objetos.Programa7
import Objetos.Programa8
import Objetos.Programa9
import Objetos.Programa10
def menu():
    salir=False
    while(salir==False):
            print("Programas con funciones")
            print("1) Pares e impares")
            print("2) Tipo elemento")
            print("3) Numeros")
            print("4) Factorial")
            print("5) Sin vocales")
            print("6) Salir")
            
            opcion=int(input("Elige el programa que deseas probar"))
            if(opcion==1):
                            Objetos.Programa6.crearObjeto()

            elif(opcion==2):
                            Objetos.Programa7.crearObjeto()
            elif(opcion==3):
                            Objetos.Programa8.crearObjeto()
            elif(opcion==4):
                            Objetos.Programa9.crearObjeto()
            elif(opcion==5):
                            Objetos.Programa10.crearObjeto()  
            elif(opcion==6):
                            salir=True
       
menu()