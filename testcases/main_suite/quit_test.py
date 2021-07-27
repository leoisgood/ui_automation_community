import unittest
import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.config_utils import local_config
from common.test_data_utils import TestDataUtils


class QuitTest(unittest.TestCase):
    test_data_utils = TestDataUtils('main_suite', 'main_suite')   # 获得一个测试数据转换的实例

    def setUp(self) -> None:
        self.base_page = BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(local_config.url)
        self.test_data = TestDataUtils('main_suite', 'main_suite').get_test_data()

    def tearDown(self) -> None:
        self.base_page.close_tab()

    @unittest.skipIf(test_data_utils.get_is_run('test_quit'), '退出成功测试用例跳过')  # 使用类属性，可以提供给实例方法使用
    def test_quit(self):
        test_case_data = self.test_data['test_quit']
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()    # 默认的登陆方式
        quit_action = QuitAction(main_page.driver)
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        self.assertTrue(actual_result.__contains__(test_case_data['expect_result']), 'test_quit用例失败')


if __name__ == '__main__':
    unittest.main()
