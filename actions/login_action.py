from elements_infos.login.login_page import LoginPage
from elements_infos.main.main_page import MainPage
from common.config_utils import local_config
from common.browser import Browser


class LoginAction:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver=self.login_page.driver)

    def login_action(self, username, password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_success(self, username, password):
        self.login_action(username, password)
        return self.main_page     # 返回主页面的对象

    def default_login(self):
        self.login_success(local_config.user_name, local_config.password)
        return self.main_page    # 返回主页面的对象

    def login_fail(self, username, password):
        self.login_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    def login_by_cookie(self):
        pass


if __name__ == '__main__':
    driver = Browser().get_driver()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    Login = LoginAction(driver)
    Login.login_success('test01', 'newdream123')
