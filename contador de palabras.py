from subprocess import BELOW_NORMAL_PRIORITY_CLASS


palabras =0
frase=input("tu frase: ")
#Solucion uno simple
for contar in range(len(frase)):
    if frase[contar]==" ":
        palabras +=1

palabras+=1
print ("Numero de palabras= ",palabras)

#Solucion 2 usando split
newstring=frase.split()#Convierte el string de entrada en una lista por palabras
print ("Con split:  ",newstring)
print("Numero de palabras: ",len(newstring))

#TODO leer de un archivo txt, uno o varios parrafos
