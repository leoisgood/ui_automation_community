import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base_page import BasePage
from elements_infos.login.login_page import LoginPage
from common.log_utils import logger
from common.browser import Browser
from common.element_data_utils import ElementDataUtils
import time

current = os.path.dirname(__file__)
driver_path = os.path.join(current, '../../webdriver/chromedriver-bak-2.exe')

"""页面作为类 控件作为属性 操作作为方法"""


class MainPage(BasePage):
    def __init__(self, driver):
        """ 登陆成功之后才能识别元素"""
        super().__init__(driver)
        elements = ElementDataUtils('main').get_element_info('main_page')
        self.companyname_showbox = elements['companyname_showbox']
        self.myzone_link = elements['myzone_link']
        self.product_menu = elements['product_menu']
        self.user_menu = elements['user_menu']
        self.quit_button = elements['quit_button']

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):    # 元素操作保持原子性
        self.click( self.quit_button )

    def get_companyname(self):  # 获取公司名称
        value = self.companyname_showbox.get_attribute('title')
        return value

    # def goto_myzone(self):  # 进入我的地盘菜单
    #     self.myzone_menu.click()
    #
    # def goto_product(self):  # 进入产品菜单
    #     self.product_menu.click()
    #
    # def get_username(self):  # 获取用户名
    #     value = self.username_showspan.text
    #     logger.info('获取用户名：' + str(value))
    #     return value


if __name__ == '__main__':
    # driver = Browser().get_driver()
    # print(driver)
    current = os.path.dirname(__file__)
    driver_path = os.path.join(current, '../../webdriver/chromedriver-bak-2.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
    login_page.wait(3)
    main_page = MainPage(driver)
    # main_page.goto_myzone()
    # main_page.goto_product()
    time.sleep(3)
    username = main_page.get_username()
    print(username)
