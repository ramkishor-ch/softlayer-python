"""Reflash firmware."""
# :license: MIT, see LICENSE for more details.

import click

import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import exceptions
from SoftLayer.CLI import formatting
from SoftLayer.CLI import helpers


@click.command(cls=SoftLayer.CLI.command.SLCommand, )
@click.argument('identifier')
@environment.pass_env
def cli(env, identifier):
    """Reflash server firmware."""

    mgr = SoftLayer.HardwareManager(env.client)
    hw_id = helpers.resolve_id(mgr.resolve_ids, identifier, 'hardware')
    if not (env.skip_confirmations or
            formatting.confirm('This will power off the server with id %s and '
                               'reflash device firmware. Continue?' % hw_id)):
        raise exceptions.CLIAbort('Aborted.')

    if mgr.reflash_firmware(hw_id):
        click.echo('Successfully device firmware reflashed')
