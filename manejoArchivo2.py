# -*- coding: utf-8 -*-

def run():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
           print(line)

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()