from selenium.webdriver import Chrome
import pytest

@pytest.fixture
def setup():
    driver=Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()


