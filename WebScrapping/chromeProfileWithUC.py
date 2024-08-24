import os
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def start_driver():
    # Define the profile directory
    profile_dir = "/Users/dev1/Documents/Reusable-Code-Collection/Profiles"

    # Check if the profile directory exists, and create it if it doesn't
    if not os.path.exists(profile_dir):
        os.makedirs(profile_dir)
        print(f"Created profile directory: {profile_dir}")
    else:
        print(f"Using existing profile directory: {profile_dir}")

    # Set Chrome options
    options = uc.ChromeOptions()

    # Initialize Chrome with the user_data_dir argument directly
    driver = uc.Chrome(user_data_dir=profile_dir, options=options)

    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the Instagram page
    driver.get(f"https://www.instagram.com/")

    # Allow time for the page to load
    time.sleep(10)

    # Return the driver instance for further actions
    return driver


driver = start_driver()

# Don't forget to close the driver when done
driver.quit()
