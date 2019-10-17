from typing import List, Any

import click
from Clients.services import ClientService
from Clients.models import Client


@click.group()
def clients():
    """Maneges de clients lifecycle V1"""
    pass


@click.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-n', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_services = ClientService(ctx.obj['clients_table'])

    client_services.create_client(client)


@click.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_services = ClientService(ctx.obj['clients_table'])
    client_list = ClientService.list_clients()

    click.echo('id  -  Name -  Company - mail -  Position')
    click.echo('*'*100)
    for client in client_list:
        click.echo('{uid} - {name} - {company} - {mail} - {position}'.format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            mail=client['mail'],
            position=client['position']
        ))

@click.command()
@click.pass_context
def update(ctx, clients_uid):
    """Update a client"""
    pass


@click.command()
@click.pass_context
def delete(ctx, clients_uid):
    """"Delete a client"""
    pass


