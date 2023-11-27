import pytest
from selenium import webdriver
from config.config import Config


@pytest.fixture()
def driver_(request):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opts)
    driver.get(Config.url)
    driver.maximize_window()
    yield driver
    driver.quit()
