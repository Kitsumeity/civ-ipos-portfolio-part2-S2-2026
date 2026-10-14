import unittest
from src.task import Task
import os

TEST_FILE = "test_tasks.bin"
TEST_DATE = ""


class TestDateUtils(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by initialising an empty task list
        and backing up the original task binary file.
        """
        self.tasks = []
        self.original_file = "tasks.bin"
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        os.rename("tasks.bin", TEST_FILE) if os.path.exists("tasks.bin") else None

    def tearDown(self):
        """
        Clean up the test environment by removing any test-created binary files
        and restoring the original task binary file.
        """
        if os.path.exists("tasks.bin"):
            os.remove("tasks.bin")
        os.rename(TEST_FILE, "tasks.bin") if os.path.exists(TEST_FILE) else None



if __name__ == "__main__":
    unittest.main()