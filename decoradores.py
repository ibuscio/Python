# -*- coding: utf-8 -*-

def protected(func):

    def wrapper(password):
        if password == 'platzi':
            func()  ##aca esta ejecutando la funcion protected_func
        else:
            print('La contraseña es incorrecta')


    return wrapper

@protected
def protected_func():
    print('La contraseña es correcta')

if __name__ == '__main__':
    password = input('Ingrese la contraseña: ')

    protected_func(password)