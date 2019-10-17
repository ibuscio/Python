# -*- coding: utf-8 -*-

class Lamp:
    _LAMPS = ['''
             .
        .    |    ,
         \   '   /
          ` ,-. '
       --- (   ) ---
            \ /
           _|=|_
          |_____|
       ''',
              '''
                   ,-.
                  (   )
                   \ /
                  _|=|_
                 |_____|
              ''']

    def __init__(self , is_turned_on):
        self.is_terned_on = is_turned_on

    def turn_on(self):           # metodo publico
        self.is_terned_on = True
        self._display_image()

    def turn_off(self):    # metodo publico
        self.is_terned_on = False
        self._display_image()

    def _display_image(self):     # metodo privado
        if self.is_terned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


def run():
    lamp = Lamp(is_turned_on = False)
    while True:
        command = str(input('''
                ¿Qué deseas hacer?

                [p]render
                [a]pagar
                [s]alir
            '''))
       ## print('Command {}'.format(command))
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()