import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """ Method get current url """

    def get_current_url(self):
        got_url = self.driver.current_url
        print(f"Current url: '{got_url}'")

    """ Method assert page title 'Products' """

    def assert_page_title(self,word, result):
        value_word = word.text
        assert value_word == result
        print(f"Page title is '{result}'")

    """ Method screenshot """

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\ilmir\\AquaProjects\\metro_shop_project\\screen\\' + name_screenshot)
