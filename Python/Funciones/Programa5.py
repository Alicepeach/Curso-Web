def invertirPalabra():
    print("Ingrese la palabra a invertir")
    palabra=input()
    palabra2=""
    for i in range(len(palabra),0,-1):
        palabra2+=palabra[i-1]
    print(palabra2)

