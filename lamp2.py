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
