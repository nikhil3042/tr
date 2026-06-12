from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
try:
    # Navigate directly to the login page
    driver.get('https://practice.expandtesting.com/notes/app/login')
    time.sleep(3)
    
    # Now look for input fields in the login form
    print('--- Looking for input fields in login form ---')
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    print(f'Total input fields found: {len(inputs)}')
    for i, inp in enumerate(inputs):
        inp_id = inp.get_attribute("id")
        inp_name = inp.get_attribute("name")
        inp_type = inp.get_attribute("type")
        inp_placeholder = inp.get_attribute("placeholder")
        inp_class = inp.get_attribute("class")
        print(f'  Input {i+1}: type="{inp_type}" id="{inp_id}" name="{inp_name}" placeholder="{inp_placeholder}" class="{inp_class}"')
    
    # Look for buttons
    print('\n--- Looking for buttons in login form ---')
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f'Total buttons found: {len(buttons)}')
    for i, btn in enumerate(buttons):
        btn_id = btn.get_attribute("id")
        btn_name = btn.get_attribute("name")
        btn_class = btn.get_attribute("class")
        btn_type = btn.get_attribute("type")
        print(f'  Button {i+1}: text="{btn.text}" type="{btn_type}" id="{btn_id}" name="{btn_name}" class="{btn_class}"')
    
    # Look for the form
    print('\n--- Looking for forms ---')
    forms = driver.find_elements(By.TAG_NAME, 'form')
    print(f'Total forms found: {len(forms)}')
    for i, form in enumerate(forms):
        form_id = form.get_attribute("id")
        form_name = form.get_attribute("name")
        form_class = form.get_attribute("class")
        print(f'  Form {i+1}: id="{form_id}" name="{form_name}" class="{form_class}"')
    
finally:
    driver.quit()

