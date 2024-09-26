from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

list1 = ["i5", "i8"]
list2 = ["i15", "i18", "i21", "i24"]

for i in range(1000):
  
  driver = webdriver.Chrome()
    
  driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfkhW2zDhKKLkNFmf4qSsmWXV6LGcgu-Q4y_Yxhf0FN0oqlcQ/viewform?usp=sf_link")

  wait = WebDriverWait(driver, 10)

  option1 = wait.until(EC.element_to_be_clickable((By.ID, random.choice(list1))))
  option1.click()
  option2 = wait.until(EC.element_to_be_clickable((By.ID, random.choice(list2))))
  option2.click()
  input_field = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd")))
  input_field.send_keys("User " , i)
  submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']")))
  submit_button.click()

  driver.quit()

  print(i)