from elements_infos.login.login_page import LoginPage
from elements_infos.main.main_page import MainPage
from common.config_utils import local_config
from common.browser import Browser


class QuitAction:
    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)


if __name__ == '__main__':
    driver = Browser().get_driver()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')