# -*- coding: utf-8 -*-
import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['lavadora', 'computadora', 'teclado', 'sofa', 'gobierno', 'diputado']


def random_word():
    aux_len = len(WORDS) - 1
    # print(' aux_len: {}'.format( aux_len))
    idx = random.randint(0, aux_len)
    # print('idx: {}'.format(idx) )
    return idx


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*---*---*---*---*---')


def run():
    id_word = random_word()
    # print('id_word:{}'.format(id_word))
    word = WORDS[id_word]
    len_word = len(word) - 1
    # print('len_word:{}'.format(len_word))
    hidden_word_mask = ['-'] * len_word
    # print('word: {}'.format(word))

    tries = 0

    while True:
        display_board(word, tries)
        current_letter = str(input('Escoge una letra:  '))

        letter_index = []
        for i in range(len_word):
            if word[i] == current_letter:
                letter_index.insert(i, current_letter)

        if len(letter_index) == 0:
            tries = tries + 1

            if tries == 7:
                display_board(word, tries)
                print('Perdiste! la palabra correcta era {}'.format(word))
        else:

            for idx in range(len(word)):
                if word[idx] == current_letter:
                    hidden_word_mask.insert(idx, current_letter)

        letter_index = []
        print(hidden_word_mask)




if __name__ == '__main__':
    print('B I E N V E N I D O S A A H O R C A D O')
    run()

