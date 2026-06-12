from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
try:
    driver.get('https://practice.expandtesting.com/notes/app')
    time.sleep(2)
    
    # Find and click the Login link
    try:
        login_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
        print(f'Found login link: {login_link.get_attribute("href")}')
        login_link.click()
        time.sleep(3)
    except Exception as e:
        print(f'Error finding login link: {e}')
    
    # Now look for input fields in the login form
    print('\n--- Looking for input fields in login form ---')
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    print(f'Total input fields found: {len(inputs)}')
    for i, inp in enumerate(inputs):
        inp_id = inp.get_attribute("id")
        inp_name = inp.get_attribute("name")
        inp_type = inp.get_attribute("type")
        inp_placeholder = inp.get_attribute("placeholder")
        print(f'  Input {i+1}: type="{inp_type}" id="{inp_id}" name="{inp_name}" placeholder="{inp_placeholder}"')
    
    # Look for buttons
    print('\n--- Looking for buttons in login form ---')
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f'Total buttons found: {len(buttons)}')
    for i, btn in enumerate(buttons):
        btn_id = btn.get_attribute("id")
        btn_name = btn.get_attribute("name")
        btn_class = btn.get_attribute("class")
        print(f'  Button {i+1}: "{btn.text}" - id="{btn_id}" name="{btn_name}" class="{btn_class}"')
    
    # Look for all elements with submit role or type
    print('\n--- Looking for submit buttons ---')
    submit_elements = driver.find_elements(By.XPATH, "//*[@type='submit']")
    print(f'Submit elements found: {len(submit_elements)}')
    for i, elem in enumerate(submit_elements):
        print(f'  Submit {i+1}: tag="{elem.tag_name}" text="{elem.text}" class="{elem.get_attribute("class")}"')
    
finally:
    driver.quit()

