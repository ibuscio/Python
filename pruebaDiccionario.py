# -*- coding: utf-8 -*-

def run():
    calificaciones= {}
    calificaciones['algoritmos'] = 9
    calificaciones['matematicas'] = 10
    calificaciones['web'] = 6
    calificaciones['base_de_datos'] = 7
    total = 0
    i = 0
    average = 0

    #for key in calificaciones:
     #   print(key)
    for key in calificaciones.values():
        print(key)

    for value in calificaciones.values():
        total = total + value
        i = i +1

    average = total / i

    return average

    # for key, value in calificaciones.items():
        # print('llave: {}, valor: {}'.format(key, value))




if __name__=='__main__':
   average =  run()
   print('El promedio es: {}'.format(average))
