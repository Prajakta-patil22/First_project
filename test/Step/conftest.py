import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/")  # get method to hit url on  browser
    driver.maximize_window()
    yield
    driver.quit()