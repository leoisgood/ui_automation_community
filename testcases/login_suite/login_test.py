import unittest
from common.browser import Browser
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    """
    登陆测试类
    """
    test_data_utils = TestDataUtils('login_suite', 'login_suite')   # 获得一个测试数据转换的实例
    test_data = TestDataUtils('login_suite', 'login_suite').get_test_data()     # 获得测试数据类

    def setUp(self) -> None:
        super().setUp()

    @unittest.skipIf(test_data_utils.get_is_run('test_login_success'), '登录成功测试用例跳过')  # 使用类属性，可以提供给实例方法使用
    def test_login_success(self):
        print(self.test_data_utils.get_is_run('test_login_success'))
        test_case_data = self.test_data['test_login_success']
        self._testMethodDoc = test_case_data['test_case_name']  # 测试用例名称
        login_action = LoginAction(self.base_page.driver)
        # 从测试用例数据中取出相应的字段（测试数据，期望结果等）
        main_page = login_action.login_success(test_case_data['test_parameter'].
                                               get('username'), test_case_data['test_parameter'].get('password'))
        actual_result = main_page.get_username()
        self.assertEqual(actual_result, test_case_data['expect_result'], 'test_login_success执行失败')
        self.base_page.screenshot_as_file()

    @unittest.skipIf(test_data_utils.get_is_run('test_login_success'), '登录失败测试用例跳过')  # 使用类属性，可以提供给实例方法使用
    def test_login_fail(self):
        test_case_data = self.test_data['test_login_fail']
        self._testMethodDoc = test_case_data['test_case_name']
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail(test_case_data['test_parameter'].
                                                get('username'), test_case_data['test_parameter'].get('password'))
        self.assertEqual(actual_result, test_case_data['expect_result'], 'test_login_success执行失败')
        self.base_page.screenshot_as_file()


if __name__ == '__main__':
    unittest.main()
