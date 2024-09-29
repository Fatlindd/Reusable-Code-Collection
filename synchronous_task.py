import threading
import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

class BrowserHandler:
    def __init__(self):
        """Initialize a browser instance with an optional user agent."""
        self.options = Options()
        self.driver = None
    
    def start_browser(self):
        """Start the undetected Chrome WebDriver."""
        self.driver = uc.Chrome(options=self.options)

    def get_driver(self):
        """Return the browser driver."""
        return self.driver

    def close_browser(self):
        """Close the browser instance."""
        if self.driver:
            self.driver.quit()

class Task:
    def __init__(self, name, url):
        """Initialize the task with a name and URL."""
        self.name = name
        self.url = url
    
    def run(self, driver):
        """Perform the task using the WebDriver."""
        print(f"Thread {self.name}: Starting task.")
        
        driver.get(self.url)
        time.sleep(2)  # Wait for the page to load (customize as needed)
        
        print(f"Thread {self.name}: Task completed on {self.url}.")

class SeleniumThread(threading.Thread):
    def __init__(self, name, task, browser_handler):
        """Initialize the thread with a task and shared browser handler."""
        threading.Thread.__init__(self)
        self.name = name
        self.task = task
        self.browser_handler = browser_handler
    
    def run(self):
        """
        Run the task in this thread.
        In the Main class, when thread.start() is called, it invokes the run() method of the SeleniumThread instance in a new thread. This means that the code inside the run() method will execute in a separate thread from the main program.
        """
        print(f"Thread {self.name}: Running...")
        driver = self.browser_handler.get_driver()
        self.task.run(driver)
        print(f"Thread {self.name}: Finished.")

class Main:
    def __init__(self):
        """Initialize the Main class to handle multi-threading."""
        self.browser_handler = BrowserHandler()

    def run_tasks(self, tasks):
        """Run the tasks synchronously using two threads."""
        self.browser_handler.start_browser()

        threads = []

        # Create a thread for each task and start them one after the other
        for i, task in enumerate(tasks):
            thread = SeleniumThread(name=f"Thread-{i+1}", task=task, browser_handler=self.browser_handler)
            threads.append(thread)
            thread.start()
            thread.join()  # Wait for the current thread to complete before starting the next

        self.browser_handler.close_browser()
        print("All tasks completed.")

if __name__ == "__main__":
    # Example usage
    task1 = Task(name="Task 1", url="https://www.google.com")
    task2 = Task(name="Task 2", url="https://www.wikipedia.org")

    main_runner = Main()
    main_runner.run_tasks([task1, task2])
