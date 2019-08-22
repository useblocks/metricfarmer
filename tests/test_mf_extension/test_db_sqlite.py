import os
import sqlite3
import shutil

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


def test_db_sqlite_new(tmpdir):
    os.chdir(tmpdir)
    sqlite_file = "new_test.db"
    if os.path.exists(sqlite_file):
        os.remove(sqlite_file)

    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/sqlite')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, "db_sqlite_new"])
    assert result.exit_code == 0
    assert 'Running db_sqlite_new: DONE' in result.output

    assert os.path.exists(sqlite_file)

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''SELECT * FROM test_table''')
    data = c.fetchone()

    assert data is not None
    assert data[0] == 'test'
    assert data[2] == '100'

    conn.commit()
    conn.close()


def test_db_sqlite_exists(tmpdir):
    """
    Checks, if values can be added, if a database file already exists.
    Adds its data to  a new table, which does not exist in the test.db file!
    """
    os.chdir(tmpdir)
    example_db_file = os.path.join(os.path.dirname(__file__), "test.db")
    sqlite_file = "test.db"
    shutil.copy(example_db_file, os.path.join(tmpdir, sqlite_file))

    if os.path.exists(sqlite_file):
        os.remove(sqlite_file)

    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/sqlite')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, "db_sqlite_exists"])
    assert result.exit_code == 0
    assert 'Running db_sqlite_exists: DONE' in result.output

    assert os.path.exists(sqlite_file)

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''SELECT * FROM test_table''')
    data = c.fetchone()

    assert data is not None
    assert data[0] == 'test'
    assert data[2] == '100'

    conn.commit()
    conn.close()
