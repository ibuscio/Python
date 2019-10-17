# -*- coding: utf-8 -*-


def manejoArchivo():
    try:
        with open('numeros.txt', 'w') as f:
            for i in range(10):
                f.write(str(i))

    except FileNotFoundError:
        print('El archivo no existe')



if __name__ == '__main__':
    manejoArchivo()