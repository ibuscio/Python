# -*- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, hight):

    mid = int((low + hight) /2)

    print('mid{}'.format(mid))
    print('numbers{}'.format(numbers[mid]))

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, hight)

if __name__ == '__main__':
    numbers = [1, 3, 4, 6, 10, 9, 11, 25, 30, 22, 34, 36, 38, 50]

    number_to_find = int(input('Ingresa un número:'))

    result = binary_search(numbers, numbers, 0, len(numbers) - 1)

    if result is True:
        print('El número si está en la lista')
    else:
        print('El número no está en la lista')
