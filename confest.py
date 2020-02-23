import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Chrome(executable_path="./chromedriver")
    driver = webdriver.Chrome("/home/geoaga/Projects/pageobject_login/chromedriver")
    yield driver
    driver.quit()
