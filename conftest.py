import pytest
from selene import browser


@pytest.fixture
def browser_setting():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    print("Open Browser")

