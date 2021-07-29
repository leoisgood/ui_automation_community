from elements_infos.login.login_page import LoginPage
from elements_infos.dashboard.dashboard_page import DashboardPage
from common.config_utils import local_config
from common.browser import Browser


class LoginAction:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver=self.login_page.driver)

    def login_by_email_action(self, email, password):
        self.login_page.click_login_link()
        self.login_page.input_email(email)
        self.login_page.input_password(password)
        self.login_page.wait(5)
        self.login_page.click_login()
        self.login_page.wait(10)    # 等待获取页面标题，完成断言

    def login_success(self, email, password):
        self.login_by_email_action(email, password)
        return self.dashboard_page     # 返回主页面的对象

    def default_login(self):
        self.login_success(local_config.user_name, local_config.password)
        return self.dashboard_page    # 返回主页面的对象

    def login_fail(self, username, password):
        self.login_by_email_action(username, password)
        return self.login_page.get_login_fail_alert_content()

    def login_by_cookie(self):
        pass


if __name__ == '__main__':
    driver = Browser().get_driver()
    driver.get('https://www.italki.live')
    Login = LoginAction(driver)
    Login.login_success('web08@qq.com', 'italki123')
