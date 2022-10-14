#generar unos dados
import random

def main():
    turno='nada'
    while turno != 'f':
        turno=input('Pulse enter para lanzar los dadoS (f + Enter para terminar)')
        turno=turno.lower()
        if turno=='f':
            break
        
        dado1=random.randint(1,6)
        dado2=random.randint(1,6)
        print ('Dado 1--> ',dado1, '  ',dado2," <-- Dado 2" )
        print(" ")
    print('Gracias por jugar ☺')


if __name__=='__main__':
    main()