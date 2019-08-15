from metricfarmer.extensions import MetricFarmerExtension

from .sources import source_static, source_random, source_file_count
from .targets import target_print, target_file_text, target_file_json, target_print_json


class MF(MetricFarmerExtension):
    def __init__(self, app):
        self.app = app

        self.name="Metric-Farmer Basics"
        self.namespace = 'mf'
        self.author = 'team useblocks'
        self.description = 'Provides basic sources and targets for Metric-Farmer'

        self.source_classes = {
            'static': source_static,
            'random': source_random,
            'file_count': source_file_count
        }

        self.target_classes = {
            'print': target_print,
            'print_json': target_print_json,
            'file_text': target_file_text,
            'file_json': target_file_json
        }


