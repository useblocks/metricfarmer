import pytest
import os

from click.testing import CliRunner
from metricfarmer.farmer import mf_cli


@pytest.mark.online
def test_rest_jira(request):
    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/rest')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, '-m', 'jira_issues' 'print'])
    assert result.exit_code == 0
    assert 'Measuring jira_issues: DONE' in result.output
    assert 'jira_issues: 0'in result.output


@pytest.mark.online
def test_rest_github_v3(request):
    farmer_folder = os.path.join(os.path.dirname(__file__), '../farmer_files/rest')
    runner = CliRunner()
    result = runner.invoke(mf_cli, ['--farmer', farmer_folder, '-m', 'github_issues', 'print'])
    assert result.exit_code == 0
    assert 'Measuring github_issues: DONE' in result.output
    assert 'github_issues: 0'in result.output
