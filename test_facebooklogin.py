import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global username,password,driver
    username = input("Enter user name")
    password = input("Enter the password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_facebooklogin(setUp):
    driver.get("https://www.facebook.com/")
    driver.find_element_by_name("email").send_keys(username)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()
    time.sleep(3)