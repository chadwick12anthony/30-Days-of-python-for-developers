import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Import this!

print(dir(webdriver))
browser = webdriver.Safari()  # or Firefox()

url = 'https://google.com'
browser.get(url)

time.sleep(2)

# Old way (doesn't work in Selenium 4.13+):
# search_el = browser.find_element_by_name("q")

# New way (works in current Selenium):
search_el = browser.find_element(By.NAME, "q")
search_el.send_keys("selenium python")

# For the submit button:
submit_btn_el = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()

# Don't forget to close the browser when done
# browser.quit()