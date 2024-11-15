import time
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SecondPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    PAGE_PRODUCT_1 = ("xpath", "//div[@data-product-inv='27']")
    PAGE_PRODUCT_2 = ("xpath", "//div[@data-product-inv='59']")
    PAGE_PRODUCT_3 = ("xpath", "//div[@data-product-inv='7']")
    ADD_TO_CART = ("xpath", "//a[@class='t762__btn t-btn t-btn_sm']")
    # CART = ("xpath", "//img[@class='tn-atom__img t-img loaded']")
    CART = ("xpath", "//a[@class='tn-atom'][@href='#opencart']")
    PAGE_TITLE = ("xpath", "//div[@class='t706__cartwin-heading t-name t-name_xl']")


# Getters
    def get_page_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PAGE_PRODUCT_1))

    def get_page_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PAGE_PRODUCT_2))

    def get_page_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PAGE_PRODUCT_2))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.ADD_TO_CART))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CART))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PAGE_TITLE))



    # Actions
    def click_select_product_1(self):
        self.get_page_product_1().click()
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.get_add_to_cart().click()
        print("Click select product 1")

    def click_select_product_2(self):
        self.get_page_product_2().click()
        self.get_add_to_cart().click()
        print("Click select product 2")

    def click_select_product_3(self):
        self.get_page_product_3().click()
        self.get_add_to_cart().click()
        print("Click select product 3")

    def click_cart(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.refresh()
        time.sleep(3)
        self.get_cart().click()
        print("Click cart")


    # Methods
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        time.sleep(5)
        self.click_cart()
        self.assert_page_title(self.get_page_title(), "Ваша корзина")


    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.driver.refresh()
        self.click_cart()
        self.assert_page_title(self.get_page_title(), "Ваша корзина")

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()
        self.assert_page_title(self.get_page_title(), "Ваша корзина")
