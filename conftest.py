import pytest
from selenium import webdriver
import yaml

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
