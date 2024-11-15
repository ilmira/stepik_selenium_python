from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains    #импорт класс ActionChains


class FirstPage(Base):

    url = "https://shop.mosmetro.ru"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    MENU_KANTSELYARIYA = ("xpath", "//a[@data-menu-item-number='5'][@href='#kantselyariya']")
    PRODUCTS_POSTERS = ("xpath", "//div/a[@data-menu-item-number='5'][@href='/posters']")
    PAGE_TITLE = ("xpath", "//div[@class='t059__text-impact t-text-impact t-text-impact_xs']/div")

    # Getters

    def get_menu_kants(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.MENU_KANTSELYARIYA))

    def get_products_posters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PRODUCTS_POSTERS))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PAGE_TITLE))

    # Actions
    def click_posters(self):
        self.get_menu_kants().click()
        self.get_products_posters().click()
        print("Open posters page")


    # Methods
    def move_to_posters_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_posters()
        self.assert_page_title(self.get_page_title(), "Открытки и постеры")