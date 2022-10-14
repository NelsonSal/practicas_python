#Funcion para descomponer en factores
factoresList=[]
def factores(a):
    NumDescomponer=a
    #factoresList=[]
    for i in[2,3,5,7,11,13]:
        modulo=0
        while modulo==0:
            modulo=NumDescomponer%i
            if modulo==0:
                factoresList.append(i)
                print (factoresList)
                NumDescomponer=NumDescomponer/i
            continue
        continue
    
    return factoresList

factores(26)
print(factoresList)


        

