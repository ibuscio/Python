

def run(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps = sum_of_temps + temp


    aux_average = float(sum_of_temps / len(temps))
    return aux_average


if __name__=='__main__':
    temps = [30, 31, 22, 20, 25]
    average = run(temps)

    print('La temperatura promedio es {}'.format(average))