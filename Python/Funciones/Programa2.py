def convertir():
        print("Bienvenido al convertidor")
        print("1)De Celsius -> Fahrenheit")
        print("2)De Fahrenheit -> Celsius")
        try:
                opcion=int(input())
                print("Cantidad a convertir:")
                tmp=int(input())
                if opcion != 1 and opcion !=2:
                        print("Opcion no valida")
                elif opcion==2:
                        return ((9/5)*tmp)+32 
                elif opcion==1:
                        return (tmp-32)*(5/9)     
        except:
                print("No haz ingresado un numero")