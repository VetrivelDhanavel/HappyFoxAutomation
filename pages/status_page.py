from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StatusPage(BasePage):
    def create_status(self, status_name, color):
        self.driver.find_element(By.LINK_TEXT, "Statuses").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click()
        self.driver.find_element(By.TAG_NAME, "input").send_keys(status_name)
        status_colour_select = self.driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        status_colour_select.click()
        status_colour_input = self.driver.find_element(By.XPATH, "//input[@class='sp-input']")
        status_colour_input.clear()
        status_colour_input.send_keys(color)
        status_colour_input.send_keys(Keys.ESCAPE)
        self.driver.find_element(By.XPATH,
                                 "//button[@class='hf-entity-footer_primary hf-primary-action ember-view']").click()
