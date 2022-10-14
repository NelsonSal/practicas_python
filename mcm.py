#generar divisor>Numeros primos
#Descomponer numero a evaluar

#saber si un numero es primo
#comenzar a dividirlo desde 2 hasta el numero(menos 1?) y si el residuo da cero en 
#algun momento, entonces no es primo


primos=[]
#hasta que numero
numeroFinal=19
for analizaprimo in range(2,numeroFinal+1):
    numero=analizaprimo
    for divisor in range (2,numero,1):
        print("entro!)")
        modulo=numero%divisor
        if modulo==0:
            print(numero , " No es primo")
            break
        continue
    if numero==2 or divisor==numero-1:
        #aca podemos poner la funcion para coemnzar a sacar factores 
        #esta funcion debe parar cuando la division de 1!!!!
        print (numero," Es primo")
        primos.append(numero)
print ("lista de primos",primos)
