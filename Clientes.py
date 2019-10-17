import sys
import csv
import os

CLIENT_TABLE ='clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clientes = []


def _initialize_clientes_from_storage():
    with open(CLIENT_TABLE, mode = 'r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clientes.append(row)

def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames= CLIENT_SCHEMA)
        writer.writerows(clientes)

        os.remove(CLIENT_TABLE)
        f.close()
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(cliente_name):
    global clientes
    if cliente_name not in clientes:
        clientes.append(cliente_name)
    else:
        print('Client already is in client\'s list')


def delete_client(client_name):
    global clientes, esta

    esta = 'N'
    for idx, cliente in enumerate(clientes):
        if cliente['name'] == client_name['name']:
            del clientes[idx]
            esta = 'S'
            break

    if esta == 'N':
        print('Client is not in clientes list')


def search_client(client_name):
    global clientes, esta
    esta = 'N'
    for idx, cliente in enumerate(clientes):
        if cliente['name'] == client_name['name']:
            print('{uid}| {name} | {company} | {email} | {position}'.format(
                uid = idx,
                name = cliente['name'],
                company = cliente['company'],
                email = cliente['email'],
                position = cliente['position']
            ))
            esta = 'S'
            break

    if esta == 'N':
        print('Client is not in clientes list')


def list_client():
    for idx, cliente in enumerate(clientes):
        print('{uid}| {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = cliente['name'],
            company = cliente['company'],
            email = cliente['email'],
            position = cliente['position']
        ))


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field


def get_cliente_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('Whats would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[L]List')
    print('[S]erch')

if __name__ == '__main__':
    _initialize_clientes_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        cliente = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(cliente)
    elif command == 'D':
            cliente = {
                'name': _get_client_field('name'),
            }
            delete_client(cliente)
    elif command == 'U':
            esta = 'N'
            client_name = {
                'name': _get_client_field('name'),
            }
            update_client_name = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position'),
            }

            for idx, cliente in enumerate(clientes):
                if cliente['name'] == client_name['name']:
                    cliente['name'] =  update_client_name['name']
                    esta = 'S'
                    break

            if esta == 'N':
                print('Client is not in clientes list')
    elif command == 'L':
            list_client()
    elif command == 'S':
            cliente = {
                'name': _get_client_field('name'),
            }
            search_client(cliente)

    else:
        Print('Error')

_save_clients_to_storage()
