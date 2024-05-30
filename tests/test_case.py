import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pages.login_page import LoginPage
from pages.status_page import StatusPage
from pages.priority_page import PriorityPage
from utils.drivers import Driver


class TestcaseHappyFox(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = Driver().get_driver()
            self.driver.get("https://interview.supporthive.com/staff/")
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
        except WebDriverException as e:
            print("WebDriverException occurred:", e)
            raise

    def test_create_status_and_priority(self):
        login_page = LoginPage(self.driver)
        login_page.login("Agent", "Agent@123")

        status_page = StatusPage(self.driver)
        status_page.create_status("Issue Created", "#47963f")

        priority_page = PriorityPage(self.driver)
        priority_page.create_priority("Assistance required", "Priority of the newly created tickets")
        priority_page.delete_priority()

    def tearDown(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "Logout").click()
        except WebDriverException as e:
            print("WebDriverException occurred during tearDown:", e)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
