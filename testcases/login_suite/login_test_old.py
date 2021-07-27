import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import local_config


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_login_success(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.login_success('test01', 'newdream123')
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, '测试人员1', 'test_login_success执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('test03', 'newdream1234')
        self.assertEqual(actual_result, '登录失败，请检查您的用户名或密码是否填写正确。', 'test_login_success执行失败')
        self.base_page.screenshot_as_file()


if __name__ == '__main__':
    unittest.main()


