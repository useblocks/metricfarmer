import os

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


def test_mf_env(tmpdir):
    os.chdir(tmpdir)
    result_file = 'mf_env_results.txt'
    os.environ['METRICFARMER_PATH'] = result_file
    assert not os.path.exists(result_file)

    farmer_folder = os.path.join(os.path.dirname(__file__), 'farmer_files/helpers/mf_env')

    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, 'test_file'])
    assert result.exit_code == 0
    assert os.path.exists(result_file)
