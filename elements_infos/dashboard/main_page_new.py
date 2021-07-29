import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.browser import Browser
from actions.login_action import LoginAction
from common.element_data_utils import ElementDataUtils
"""页面作为类 控件作为属性 操作作为方法"""


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils('main_page').get_element_info('login_page')
        self.myzone_link = elements['myzone_link']
        self.user_menu = elements['user_menu']

    def goto_myzone(self):  # 进入我的地盘菜单
        self.click(self.myzone_link)

    def get_username(self):
        value = self.get_text(self.user_menu)
        return value


if __name__ == '__main__':
    driver = Browser().get_driver()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    main_page = LoginAction(driver).default_login()
    main_page.get_username()
    main_page.goto_myzone()


