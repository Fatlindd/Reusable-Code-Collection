import asyncio

class Task:
    def __init__(self, task_name, duration):
        """
        Initialize a task with a name and duration.

        :param task_name: str - Name of the task.
        :param duration: int - Time in seconds that the task will take to complete.
        """
        self.task_name = task_name
        self.duration = duration

    async def run(self):
        """
        Simulates running the task asynchronously by awaiting the sleep for the task's duration.
        """
        print(f"Starting task: {self.task_name}")
        await asyncio.sleep(self.duration)  # Asynchronous sleep
        print(f"Task {self.task_name} completed after {self.duration} seconds")


class TaskManager:
    def __init__(self):
        """
        Initialize the TaskManager with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task_name, duration):
        """
        Adds a task to the task list.

        :param task_name: str - Name of the task.
        :param duration: int - Duration for the task.
        """
        task = Task(task_name, duration)
        self.tasks.append(task)

    async def run_tasks(self):
        """
        Runs all tasks asynchronously.
        """
        print("Running tasks asynchronously...")
        tasks = [task.run() for task in self.tasks]  # Prepare the list of task coroutines
        await asyncio.gather(*tasks)  # Run tasks concurrently
        print("All tasks completed!")


# Example usage
if __name__ == "__main__":
    task_manager = TaskManager()
    
    # Adding tasks
    task_manager.add_task("Download File", 2)
    task_manager.add_task("Process Data", 3)
    task_manager.add_task("Upload Results", 1)
    
    # Running tasks asynchronously
    asyncio.run(task_manager.run_tasks())
