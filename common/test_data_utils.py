#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/7/23 23:39
# @E-mail: leo.liu@italki.com
import os
import yaml
from common.config_utils import local_config

cur_path = os.path.dirname(__file__)
yaml_path = os.path.join(cur_path, '..', local_config.testdata_path)


class TestDataUtils:
    def __init__(self, test_suite_name, test_suite):
        self.test_suite_path = os.path.join(yaml_path, test_suite_name, test_suite_name) + '.yaml'
        self.test_suite_name = test_suite_name
        self.test_suite = test_suite
        self.test_data = self.get_test_data()

    def get_test_data(self):
        with open(self.test_suite_path, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
            test_data = {}
            for i, j in data.items():  # 取出字典里的键值对，存入新的字典
                if j['test_suite'] == self.test_suite:
                    test_data[i] = j
        return test_data

    def get_param_data(self, key1, key2):
        return self.test_data[key1][key2]

    def get_is_run(self, test_function_name):
        return False if self.test_data[test_function_name]['is_run'].__eq__('是') else True


if __name__ == '__main__':
    testdatautils = TestDataUtils('login_suite', 'login_suite')
    test_datas = testdatautils.get_test_data()
    test_suite_path = testdatautils.test_suite_path
    print(testdatautils.get_is_run('test_login_success'), testdatautils.test_data)
