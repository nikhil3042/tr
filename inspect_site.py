from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
try:
    driver.get('https://practice.expandtesting.com/notes/app')
    time.sleep(3)
    
    # Get page source to inspect
    print('Page Title:', driver.title)
    print('\n--- Looking for login button ---')
    
    # Try different selectors for login button
    try:
        login_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        print('Found login button with text')
    except:
        pass
    
    try:
        login_btn = driver.find_element(By.XPATH, "//a[contains(text(), 'Login')]")
        print('Found login link')
    except:
        pass
    
    # Look for all buttons
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    print(f'\nTotal buttons found: {len(buttons)}')
    for i, btn in enumerate(buttons):
        print(f'  Button {i+1}: "{btn.text}" - id="{btn.get_attribute("id")}" - class="{btn.get_attribute("class")}"')
    
    # Look for all links
    links = driver.find_elements(By.TAG_NAME, 'a')
    print(f'\nTotal links found: {len(links)}')
    for i, link in enumerate(links[:15]):
        text = link.text.strip()
        if text:
            href = link.get_attribute("href")
            print(f'  Link {i+1}: "{text}" - href: "{href}"')
    
    # Look for input fields
    print('\n--- Looking for input fields ---')
    inputs = driver.find_elements(By.TAG_NAME, 'input')
    print(f'Total input fields found: {len(inputs)}')
    for i, inp in enumerate(inputs):
        inp_id = inp.get_attribute("id")
        inp_name = inp.get_attribute("name")
        inp_type = inp.get_attribute("type")
        inp_placeholder = inp.get_attribute("placeholder")
        print(f'  Input {i+1}: type="{inp_type}" id="{inp_id}" name="{inp_name}" placeholder="{inp_placeholder}"')
    
finally:
    driver.quit()

