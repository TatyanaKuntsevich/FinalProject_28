from selenium import webdriver
import pytest
from config import TestData



@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.chrome_driver)
        web_driver.set_window_size(TestData.width, TestData.length)
    request.cls.driver = web_driver


    yield

    web_driver.quit()

