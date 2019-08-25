import pytest


def pytest_addoption(parser):
    parser.addoption('--online', action='store_true', dest="online",
                     default=False, help="enable tests which need a working connection the the internet")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "online: mark test to only with working internet connection"
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--online"):
        return
    online = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "online" in item.keywords:
            item.add_marker(online)
