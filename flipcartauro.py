import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
product=input("enter the product to be searched:")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test started")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element_by_name("q").send_keys(product)
time.sleep(1)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(5)
driver.close()
print("test completed !!")