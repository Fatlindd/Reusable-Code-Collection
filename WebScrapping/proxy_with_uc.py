import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class ProxyManager:
    def __init__(self, ip_address, port, country):
        self.ip_address = ip_address
        self.port = port
        self.country = country

    def get_proxy(self):
        return f"{self.ip_address}:{self.port}"

class WebDriverManager:
    def __init__(self, proxy_manager):
        self.proxy_manager = proxy_manager
        self.driver = self.create_driver()

    def create_driver(self):
        options = uc.ChromeOptions()
        proxy = self.proxy_manager.get_proxy()
        options.add_argument(f'--proxy-server=http://{proxy}')
        
        # Optional: Add additional options like headless mode
        # options.add_argument('--headless')  # Uncomment for headless mode

        driver_service = Service()
        driver = uc.Chrome(service=driver_service, options=options)
        return driver

    def open_google(self):
        self.driver.get("https://example.com/")
        time.sleep(10)  # Wait for a few seconds to see the page

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    # Proxy details
    ip_address = "170.254.92.198"
    port = "4153"
    country = "United Kingdom"

    # Create a ProxyManager instance
    proxy_manager = ProxyManager(ip_address, port, country)

    # Create a WebDriverManager instance with the proxy
    web_driver_manager = WebDriverManager(proxy_manager)

    # Open Google using the proxy
    web_driver_manager.open_google()

    # Close the driver
    web_driver_manager.close_driver()
