# -*- coding: utf-8 -*-
import random


def run():
    palindromo = True
    random_number = random.randint(0, 20)
    palabra = input('Ingresa una palabra:  ')
    longitud = len(palabra)
    i = 0

    while longitud > 0 and palindromo == True:
        if palabra[i] == palabra[longitud-1]:
            print(palabra[i])
        else:
            palindromo = False

        longitud = longitud -1
        i = i + 1

    if palindromo == True:
        print('La palabra ingresada es Palindromo')
    else:
        print('La palabra ingresada no es Palindromo')

if __name__ == '__main__':
    run()