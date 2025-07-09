from selenium.webdriver.common.by import By

class FinishPage:
    def __init__(self, driver):
        self.driver = driver

    def finish(self):
        self.driver.find_element(By.ID, "finish").click()

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
