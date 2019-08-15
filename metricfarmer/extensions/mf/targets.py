import click
from colorama import Fore, Style
import json
import os

from metricfarmer.exceptions import ExtensionException


def target_print(metrics, **kwargs):
    click.echo()
    for name, metric in metrics.items():
        click.echo('  {name}: '.format(name=name) + Fore.GREEN + str(metric['result']) + Style.RESET_ALL)


def target_print_json(metrics, **kwargs):
    metrics_json = json.dumps(metrics, indent=4)
    click.echo(metrics_json)


def target_file_text(metrics, **kwargs):
    if 'path' not in kwargs:
        raise ExtensionException('Path parameter must be specified for mf.file')

    path = kwargs['path']
    override = kwargs.get('override', False)
    if os.path.exists(path) and not override:
        raise ExtensionException('Given file already exists. Set override parameter to True tpo avoid this. '
                                 'Path: {}'.format(path))

    with open(path, 'w') as result_file:
        for name, metric in metrics.items():
            result_file.write('{metric}: {result}\n'.format(
                metric=name, result=metric['result']
            ))


def target_file_json(metrics, **kwargs):
    if 'path' not in kwargs:
        raise ExtensionException('Path parameter must be specified for mf.file')

    path = kwargs['path']
    override = kwargs.get('override', False)
    if os.path.exists(path) and not override:
        raise ExtensionException('Given file already exists. Set override parameter to True tpo avoid this. '
                                 'Path: {}'.format(path))

    metrics_json = json.dumps(metrics, indent=4)
    with open(path, 'w') as result_file:
        result_file.writelines(metrics_json)
