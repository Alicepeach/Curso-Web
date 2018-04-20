def multiplos():
    x=1500
    multiplosTres=[]
    multiplosCinco=[]
    while(x<=2700):
        if(x%3 == 0):
            multiplosTres.append(x)
        if(x%5==0):
            multiplosCinco.append(x)
        x+=1
    print("Multiplos de 3")
    print(multiplosTres)
    print("_________________________")
    print("Multiplos de 5")
    print(multiplosCinco)