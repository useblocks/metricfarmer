import os
import shutil

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


def test_csv_new(tmpdir):
    os.chdir(tmpdir)
    csv_file = "new.csv"
    if os.path.exists(csv_file):
        os.remove(csv_file)

    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/csv')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, "file_csv_new"])
    assert result.exit_code == 0

    assert os.path.exists(csv_file)
    with open(csv_file, 'r') as data_file:
        data = data_file.readlines()
    assert 'test,100' in "".join(data)


def test_csv_exists(tmpdir):
    # Move an existing csv-file to the tmp-dir
    example_csv_file = os.path.join(os.path.dirname(__file__), "test.csv")
    csv_file = 'exists.csv'
    shutil.copy(example_csv_file, os.path.join(tmpdir, csv_file))

    os.chdir(tmpdir)

    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/csv')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, "file_csv_exists"])
    assert result.exit_code == 0

    assert os.path.exists(csv_file)
    with open(csv_file, 'r') as data_file:
        data = data_file.readlines()

    # Check if new data got added
    assert 'test,100,100' in "".join(data)
