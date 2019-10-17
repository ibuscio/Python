

def exchange_calculator(ammount):
    tipo_de_cambio = 35
    monto_pesos = tipo_de_cambio * ammount

    return monto_pesos

def run():
    print('Convierte de U$S a pesos uruguayos')
    ammount = float(input('Ingresa el monto en dolares'))

    monto_pesos = exchange_calculator(ammount)
    print('El monto en pesos uruguayos es{}'.format(monto_pesos))


if __name__=='__main__':
    run()