
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PriorityPage(BasePage):
    def create_priority(self, priority_name, description):
        self.driver.find_element(By.LINK_TEXT, "Priorities").click()
        self.driver.find_element(By.XPATH, "//header/button[1]").click()
        self.driver.find_element(By.TAG_NAME, "input").send_keys(priority_name)
        self.driver.find_element(By.TAG_NAME, "textarea").send_keys(description)
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']").click()

    def delete_priority(self):
        self.driver.find_element(By.LINK_TEXT, "Priorities").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, "//tr[last()]/td[2]").click()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']").click()
