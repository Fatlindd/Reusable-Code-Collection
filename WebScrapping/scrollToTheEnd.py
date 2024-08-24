import os
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = None
def scroll_until_the_end():
    try:
        web_element_to_scroll = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "XPATH for the web element to scroll until the end.",
                )
            )
        )

        last_height = driver.execute_script("return arguments[0].scrollHeight", web_element_to_scroll)
        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", web_element_to_scroll)
            time.sleep(1.5)
            new_height = driver.execute_script("return arguments[0].scrollHeight", web_element_to_scroll)
            if new_height == last_height:
                break
            last_height = new_height

    except Exception as e:
        print(f"Something went wrong with scrolling: {e}")