from selenium import webdriver
import time

# Path to the existing Chrome profile directory
# /Users/dev1/Desktop/Python Examples
chrome_profile_directory = '/Users/dev1/Desktop/Python Scripts/Profiles/nordVPN-FR'

try:
    # Configure Chrome options to use the specified profile
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={chrome_profile_directory}")

    # Initialize the Chrome webdriver with the existing profile
    driver = webdriver.Chrome(options=options)

    # Example usage: navigate to a website
    driver.get("https://www.google.com")
    time.sleep(40)

    # Quit the browser and end the program
    driver.quit()

except Exception as e:
    print(f"Error occurred: {e}")


# 1. Australia -> nordVPN-Australia (PO)
# 2. Canada -> nordVPN-CA (PO)
# 3. Germany -> nordVPN-DE (PO)
# 4. France -> nordVPN-FR (PO)  
# 5. Japan -> nordVPN-Japan (PO)
# 6. Spain -> nordVPN-Spain (PO)
# 7. Switzerland -> nordVPN-Switzerland (PO)
# 8. United Kingdom -> nordVPN-UK (PO)
# 9. America -> nordVPN-US (PO)
