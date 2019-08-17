import os

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


def test_targets_default():
    farmer_folder = os.path.join(os.path.dirname(__file__), 'farmer_files/settings/targets_default')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder])
    result.exit_code == 0
    # Be sure "print" target got executed
    assert 'Running print:' in result.output


def test_targets_always():
    farmer_folder = os.path.join(os.path.dirname(__file__), 'farmer_files/settings/targets_always')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, 'print'])
    result.exit_code == 0
    # Be sure "print" target got executed
    assert 'Running print_json:' in result.output
