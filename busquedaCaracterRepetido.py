# -*- coding: utf-8 -*-

def repeat_search(listaCaracteres):
    seen_letter = []
    repeat_letter = '_'

    for idx, letter in enumerate(listaCaracteres):
        if letter not in seen_letter:
            seen_letter.insert(idx, letter)
        else:
            repeat_letter = letter

    return repeat_letter

if __name__ == '__main__':

    listaCaracteres = str(input('Ingresa una lista de caracteres sin espacios:'))
    repeat_letter = repeat_search(listaCaracteres)

    if repeat_letter != '_':
        print('El primer caracter de la lista repetido es: {}'.format(repeat_letter))
    else:
        print('No hay caracteres repetidos en la lista')


