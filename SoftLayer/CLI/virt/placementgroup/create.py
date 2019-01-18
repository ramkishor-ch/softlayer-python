"""Create a placement group"""

import click

from SoftLayer.CLI import environment
from SoftLayer.CLI import formatting
from SoftLayer.managers.vs_placement import PlacementManager as PlacementManager

from pprint import pprint as pp

def _get_routers(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return
    env = ctx.ensure_object(environment.Environment)
    manager = PlacementManager(env.client)
    routers = manager.get_routers()
    env.fout(get_router_table(routers))
    ctx.exit()

@click.command()
@click.option('--name', type=click.STRING, required=True, prompt=True, help="Name for this new placement group.")
@click.option('--backend_router_id', '-b', type=click.INT, required=True, prompt=True,
              help="backendRouterId, use --list_routers/-l to print out a list of available ids.")
@click.option('--list_routers', '-l', is_flag=True, callback=_get_routers, is_eager=True,
              help="Prints available backend router ids and exit.")
@environment.pass_env
def cli(env, **args):
    """Create a placement group"""
    manager = PlacementManager(env.client)
    placement_object = {
        'name': args.get('name'),
        'backendRouterId': args.get('backend_router_id'),
        'ruleId': 1 # Hard coded as there is only 1 rule at the moment
    }

    result = manager.create(placement_object)
    click.secho("Successfully created placement group: ID: %s, Name: %s" % (result['id'], result['name']), fg='green')


def get_router_table(routers):
    table = formatting.Table(['Datacenter', 'Hostname', 'Backend Router Id'], "Available Routers")
    for router in routers:
        datacenter = router['topLevelLocation']['longName']
        table.add_row([datacenter, router['hostname'], router['id']])
    return table




