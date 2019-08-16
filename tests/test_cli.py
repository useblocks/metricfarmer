import os

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


def test_help():
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--help'])
    assert result.exit_code == 0

    # Use "mf_cli" instead of "metricfarmer" in test, as click uses the name of the executed call as name and
    # this differs in our tests from real world.
    assert "Usage: mf_cli [OPTIONS] [TARGETS]..." in result.output


def test_empty_call():
    runner = CliRunner()
    result = runner.invoke(mf_cli, [])
    assert result.exit_code == 0


def test_empty_call_with_farmer_folder():
    os.chdir(os.path.join(os.path.dirname(__file__), 'farmer_files'))
    runner = CliRunner()
    result = runner.invoke(mf_cli, [])
    assert result.exit_code == 0

    # Be sure right farm file was loaded
    assert 'test.farm: DONE' in result.output

    # Be sure farm-file outside .farmer got not loaded
    assert 'my_metrics.farm: DONE' not in result.output


def test_spec_farmer_folder():
    farmer_folder = os.path.join(os.path.dirname(__file__), 'farmer_files/.farmer')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder])
    assert result.exit_code == 0

    # Be sure right farm file was loaded
    assert 'test.farm: DONE' in result.output

    # Be sure farm-file outside .farmer got not loaded
    assert 'metrics.farm' not in result.output
    assert 'sources.farm' not in result.output
    assert 'targets.farm' not in result.output
