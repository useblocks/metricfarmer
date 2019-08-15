import glob
import os
import random
import time


def source_static(**kwargs):
    if 'value' in kwargs.keys():
        return kwargs['value']
    return None


def source_random(**kwargs):
    min = kwargs.get('min', 0.0)
    max = kwargs.get('max', 100.0)
    digits = kwargs.get('digits', 2)
    sleep = kwargs.get('sleep', 0)

    time.sleep(sleep)

    return round(random.uniform(min, max), digits)


def source_file_count(**kwargs):
    path = kwargs.get('path', os.getcwd())
    pattern = kwargs.get('pattern', '**/*')

    file_list = glob.glob(path + '/' + pattern, recursive=True)
    return len(file_list)

