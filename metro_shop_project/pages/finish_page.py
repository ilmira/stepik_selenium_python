from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinishPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CLOSE_BUTTON = ("xpath", "//button[@class='t706__close-button t706__cartwin-close-wrapper']")


    # Getters
    def get_close_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CLOSE_BUTTON))

    # Actions
    def click_close_btn(self):
        self.get_close_btn().click()
        print("Click close button")

    # Methods
    def finish_screenshot_and_close(self):
        self.get_current_url()
        self.get_screenshot()
        self.click_close_btn()