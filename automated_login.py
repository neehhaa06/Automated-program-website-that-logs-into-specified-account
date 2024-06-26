from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def gmail_login(username, password):
    driver = webdriver.Chrome()  # Make sure to have the ChromeDriver installed and in PATH
    driver.get("https://accounts.google.com/")

    email_input = driver.find_element_by_id("identifierId")
    email_input.send_keys(username)
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)

    password_input = driver.find_element_by_name("password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(2)

    # Add any additional steps to navigate or interact with the account
    time.sleep(5)  # Allow some time for interactions or verifications

    driver.quit()

# Test the function
gmail_login('your-email@gmail.com', 'your-password')
