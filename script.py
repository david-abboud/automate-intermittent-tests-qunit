from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('Partner | Acceptance | Renew Employer | Manage Members | Main: Renew Employer - Members - Only 1 Census Export request is done')


refresh_count = 0

try:
  while True:
    try:
      driver.find_element(By.CSS_SELECTOR, "#qunit-abort-tests-button")
      tests_finished = False
    except NoSuchElementException:
      tests_finished = True

    if tests_finished:
      try:
        driver.find_element(By.CSS_SELECTOR, ".qunit-pass")
      except NoSuchElementException:
        print('Test failed!')
        break
      driver.refresh()
      refresh_count += 1
      print(f"Refresh count: {refresh_count}")
      

finally:
    print('Done')
