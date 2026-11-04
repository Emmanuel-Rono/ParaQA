import pytest
from helium import kill_browser

@pytest.fixture(autouse=True)
def cleanup_browser():
    # Teardown: ensure browser closes cleanly after each test finishes
    yield
    kill_browser()