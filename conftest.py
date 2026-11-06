from pathlib import Path
from dotenv import load_dotenv
import pytest
from helium import kill_browser

load_dotenv(Path(__file__).resolve().parent / ".env")

@pytest.fixture(autouse=True)
def cleanup_browser():
    # Teardown: ensure browser closes cleanly after each test finishes
    yield
    kill_browser()