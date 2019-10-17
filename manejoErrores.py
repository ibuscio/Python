# -*- coding: utf-8 -*-

countries = {'mexico': 122, 'colombia': 49, 'argentina': 43, 'chile': 18, 'peru': 31}

def poblacion():

    while True:
        country = str(input('Ingrese el nombre del país: ')).lower()
        try:
            print('La población de {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            print('No tenemos el dato de la población de {}'.format(country))

if __name__ == '__main__':
    poblacion()