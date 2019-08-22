import click
from colorama import Fore, Style
import csv
import datetime
import json
import os
import sqlite3

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
        raise ExtensionException('Path parameter must be specified for mf.file_text')

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
        raise ExtensionException('Path parameter must be specified for mf.file_json')

    path = kwargs['path']
    override = kwargs.get('override', False)
    if os.path.exists(path) and not override:
        raise ExtensionException('Given file already exists. Set override parameter to True tpo avoid this. '
                                 'Path: {}'.format(path))

    metrics_json = json.dumps(metrics, indent=4)
    with open(path, 'w') as result_file:
        result_file.writelines(metrics_json)


def target_file_csv(metrics, **kwargs):
    if 'path' not in kwargs:
        raise ExtensionException('Path parameter must be specified for mf.file_csv')

    path = kwargs['path']
    override = kwargs.get('override', False)
    delimiter = kwargs.get('delimiter', ',')

    orig_data = {}

    if os.path.exists(path) and not override:
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            headers = reader.fieldnames
            for row in reader:
                orig_data[row['metric']] = row
    else:
        headers = ['metric']

    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    updated_data = orig_data
    for name, metric in metrics.items():
        if name in updated_data.keys():
            updated_data[name][timestamp] = metric['result']
        else:
            updated_data[name] = {'metric': name, timestamp: metric['result']}

    # Update headers with newest timestamp for current data
    headers.append(timestamp)

    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, headers, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(updated_data.values())


def target_sqlite(metrics, **kwargs):
    path = kwargs.get('path', 'metric_results.db')
    table = kwargs.get('table', 'metrics')
    table = table.replace(',', '').replace(';', '')  # Really insecure security solution
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists {table}
                  (metric text, timestamp text, result text)'''.format(table=table))

    timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
    values = []
    for name, metric in metrics.items():
        values.append((name, timestamp, metric['result']))

    c.executemany('INSERT INTO {table} VALUES (?,?,?)'.format(table=table), values)

    conn.commit()
    conn.close()
