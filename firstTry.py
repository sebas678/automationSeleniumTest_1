from selenium import webdriver
from selenium.webdriver.support.ui import Select


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://demoqa.com/automation-practice-form')
driver.find_element_by_id("firstName").send_keys('Pepito')
driver.find_element_by_id("lastName").send_keys('PatasLargas')
driver.find_element_by_id("userEmail").send_keys('pepito@patas.largas')

if driver.find_element_by_id("gender-radio-1"):
    print("YUP")
    element=driver.find_element_by_id("gender-radio-1").click()
    driver.execute_script("arguments[0].click();", element)

#for i in range(1,4):
#    driver.find_element_by_id("gender-radio-"+str(i)).click()
