import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
"""页面作为类 控件作为属性 操作作为方法"""


class LoginPage(BasePage):
    def __init__(self, login_driver):
        super().__init__(login_driver)
        elements = ElementDataUtils('login').get_element_info('login_page')
        self.login_link = elements['login_link']
        self.email_inputbox = elements['email_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']
        # self.bug_link = elements['bug_link']

    # def click_bug_link(self, bug_title='2021-06-23'):
    #     self.bug_link = self.bug_link.locator_value % bug_title
    #     self.click(self.bug_link)

    def click_login_link(self):
        self.login_link = self.login_link
        self.click(self.login_link)

    def input_email(self, username):  # 方法 ==》 控件的操作
        self.input(self.email_inputbox, username)

    def input_password(self, password):
        self.input(self.password_inputbox, password)

    def click_login(self):
        self.click(self.login_button)
        logger.info('登录按钮是%s' % self.login_button)

    def get_login_fail_alert_content(self):
        return self.switch_to_alert()


if __name__ == '__main__':
    current = os.path.dirname(__file__)
    driver_path = os.path.join(current, '../../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=driver_path)
    login_page = LoginPage(driver)
    login_page.open_url('https://www.italki.live')
    # e1 = driver.find_element(By.XPATH, '//div[@data-cy="hp-menu-signin"]').click()
    login_page.set_browser_max()
    login_page.click_login_link()
    login_page.input_email('web08@qq.com')
    login_page.input_password('italki123')
    login_page.click_login()
    login_page.wait(3)
    login_page.screenshot_as_file()
    login_page.close_tab()

