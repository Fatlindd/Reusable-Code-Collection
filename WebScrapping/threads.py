import time
import threading
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import random


class ChromeSession:
    """Class to manage a Chrome browser session."""

    def __init__(self, thread_id: int, user_agent: str) -> None:
        """
        Initialize a new ChromeSession with a specific user agent.

        Args:
            thread_id (int): The identifier for the thread.
            user_agent (str): The user agent to be used for the session.
        """
        self.thread_id = thread_id
        self.user_agent = user_agent
        self.driver = None

    def start(self) -> None:
        """Start the Chrome session."""
        self.driver = self._initialize_driver()
        self.driver.get("https://www.example.com")
        
        time.sleep(10)  # Wait for the page to load
        print(f"Thread {self.thread_id} started with user agent: {self.user_agent}")
        time.sleep(60)  # Simulate some work with the browser

        self.quit()

    def _initialize_driver(self) -> uc.Chrome:
        """Initialize and return a new Chrome driver instance with the user agent."""
        options = uc.ChromeOptions()
        options.headless = False
        options.add_argument(f"--user-agent={self.user_agent}")
        
        driver = uc.Chrome(options=options)
        driver.set_window_size(500, 750)
        return driver

    def quit(self) -> None:
        """Close the Chrome session."""
        if self.driver:
            self.driver.quit()
            print(f"Thread {self.thread_id} finished.")


class ThreadManager:
    """Class to manage multiple threads running Chrome sessions."""

    def __init__(self, num_threads: int, file_path: str) -> None:
        """
        Initialize a ThreadManager.

        Args:
            num_threads (int): The number of threads to manage.
            file_path (str): Path to the file containing user agents.
        """
        self.num_threads = num_threads
        self.file_path = file_path
        self.user_agents = self.load_user_agents()

    def load_user_agents(self) -> list[str]:
        """Load the user agents from the given file."""
        with open(self.file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]

    def run(self) -> None:
        """Start the threads to run Chrome sessions."""
        threads = []
        
        # Ensure there are enough user agents for the number of threads
        if self.num_threads > len(self.user_agents):
            raise ValueError("Not enough user agents for the number of threads.")
        
        # Randomly assign different user agents to each thread
        selected_user_agents = random.sample(self.user_agents, self.num_threads)

        for i, user_agent in enumerate(selected_user_agents, start=1):
            session = ChromeSession(i, user_agent)
            thread = threading.Thread(target=session.start)
            threads.append(thread)
            thread.start()

            # Wait 3 seconds before starting the next thread
            time.sleep(3)

        # Wait for all threads to finish
        for thread in threads:
            thread.join()


def main() -> None:
    """Main function to execute the program."""
    num_threads = 2
    file_path = "useragents.txt"
    
    manager = ThreadManager(num_threads, file_path)
    manager.run()


if __name__ == "__main__":
    main()


# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)