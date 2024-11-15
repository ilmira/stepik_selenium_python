import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.finish_page import FinishPage
from pages.first_page import FirstPage
from pages.second_page import SecondPage

def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test 1")

    fp = FirstPage(driver)
    fp.move_to_posters_page()

    sp = SecondPage(driver)
    sp.select_product_1()

    cp = CartPage(driver)
    cp.input_information(1)


    f = FinishPage(driver)
    f.finish_screenshot_and_close()

    time.sleep(3)
    driver.quit()

# def test_buy_product_2():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#     print("Start Test 2")
#
#     fp = FirstPage(driver)
#     fp.move_to_posters_page()
#
#     sp = SecondPage(driver)
#     sp.select_product_2()
#
#     cp = CartPage(driver)
#     cp.input_information(2)
#
#
#     f = FinishPage(driver)
#     f.finish_screenshot_and_close()
#
#     time.sleep(3)
#     driver.quit()
#
# def test_buy_product_3():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#     print("Start Test 1")
#
#     fp = FirstPage(driver)
#     fp.move_to_posters_page()
#
#     sp = SecondPage(driver)
#     sp.select_product_3()
#
#     cp = CartPage(driver)
#     cp.input_information(3)
#
#
#     f = FinishPage(driver)
#     f.finish_screenshot_and_close()
#
#     time.sleep(3)
#     driver.quit()
