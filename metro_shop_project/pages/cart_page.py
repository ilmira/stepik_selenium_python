from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NOT_MIN_SUM = ("xpath", "//div[@class='t706__cartwin-prodamount-minorder t706__minimal']")
    ONE_MORE_PRODUCT = ("xpath", "//span[@class='t706__product-plus']")
    NAME = ("xpath", "//input[@data-tilda-rule='name']")
    EMAIL = ("xpath", "//input[@data-tilda-rule='email']")
    PHONE = ("xpath", "//input[@name='tildaspec-phone-part[]']")
    TIME_RADIO_BTN = ("xpath", "//label[@class='t-radio__item t-radio__control t-text t-text_xs'][2]")
    DELIVERY_RADIO_BTN = ("xpath", "//label[@data-service-id='2114716602']")
    AGREEMENT_CHECKBOX = ("xpath", "//div[@class='t-checkbox__indicator']")


    # Getters
    def get_not_min_sum(self):
        try:
            return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.NOT_MIN_SUM))
        except Exception:
            return False

    def get_one_more_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.ONE_MORE_PRODUCT))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.NAME))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.EMAIL))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.PHONE))

    def get_time_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.TIME_RADIO_BTN))

    def get_delivery_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.DELIVERY_RADIO_BTN))

    def get_agreement_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.AGREEMENT_CHECKBOX))


    # Actions
    def click_one_more_product(self, number):
        self.get_one_more_product().click()
        print(f"Click select one more product {number}")

    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone number")

    def click_time_btn(self):
        self.get_time_btn().click()
        print("Click time to delivery radio button")

    def click_delivery_btn(self):
        self.get_delivery_btn().click()
        print("Click delivery from shop radio button")

    def click_agreement_btn(self):
        self.get_agreement_btn().click()
        print("Click agreement checkbox")


    # Methods
    def input_information(self,number_of_test):
        self.get_current_url()
        while self.get_not_min_sum():
            self.click_one_more_product(number_of_test)
        self.input_name("Kate")
        self.input_email("kate@test.ts")
        self.input_phone("9999999999")
        self.click_time_btn()
        self.click_delivery_btn()
        self.click_agreement_btn()