import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.config_utils import local_config
from common.log_utils import logger
from common.browser import Browser


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        # self.chains = ActionChains(self.driver) 不推荐 每个页面都要实例化对象

    # 浏览器操作封装 -- > 二次封装
    def open_url(self, url):
        try:
            self.driver.get(url)
            logger.info('打开url地址:%s' % url)
        except Exception as e:
            logger.error('不能打开指定的测试网址，原因是%s' % e.__str__())

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def close_tab(self):
        self.driver.close()
        logger.info('关闭当前tab页签')

    def exit_driver(self):
        self.driver.quit()
        logger.info('退出浏览器')

    def get_title(self):
        value = self.driver.title
        logger.info('获取网页标题，标题是：%s' % value)
        return value

    # 元素操作封装
    def find_element(self, element_info):
        """
        根据提供的元素信息参数，进行元素定位

        :param element_info:元素信息，字典类型{....}
        :return: element对象
        """
        try:
            locator_type_name = element_info['locator_type']
            locator_value_info = element_info['locator_value']
            locator_timeout = element_info['time_out']
            if locator_type_name == 'id':
                locator_type = By.ID
            elif locator_type_name == 'class':
                locator_type = By.CLASS_NAME
            elif locator_type_name == 'xpath':
                locator_type = By.XPATH
            element = WebDriverWait(self.driver, float(locator_timeout)) \
                .until(lambda x: x.find_element(locator_type, locator_value_info))  # 显示等待
            logger.info('[%s]元素识别成功' % element_info['element_name'])
            return element
        except Exception as e:
            logger.error('[%s]元素不能识别，原因是%s' % (element_info['element_name'], e.__str__()))
            self.screenshot_as_file()
        # finally:
        #     if element is None:
        #         element = ''

    def click(self, element_info):
        element = self.find_element(element_info)
        try:
            element.click()
            logger.info('[%s]元素点击成功' % element_info['element_name'])
        except Exception as e:
            logger.error('[%s]元素点击成功,原因是%s' % (element_info['element_name'], e.__str__()))

    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容[%s]' % (element_info['element_name'], content))

    def get_text(self, element_info):
        element = self.find_element(element_info)
        return element.text

    # 等待操作封装
    def wait(self, seconds=5):
        time.sleep(seconds)
        logger.info('等待[%s]秒' % seconds)

    def implicitly_wait(self, seconds=local_config.time_out):
        self.driver.implicitly_wait(seconds)

    def chains(self):
        return ActionChains(self.driver)

    def move_to_element_by_mouse(self, element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    def long_press_element(self, element_info, seconds):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(seconds).release(element_info)

    # selenium执行js
    def execute_script(self, js_str, element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str, None)

    def delete_element_attribute(self, element_info, attribute_name):
        element = self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");' % attribute_name, element)

    def update_element_attribute(self, element_info, attribute_name, attribute_value):
        element = self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");' % (attribute_name, attribute_value), element)

    # 思路一：使用元素信息去切换frame
    def switch_to_frame_by_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路二：使用id或者name切换frame
    def switch_to_frame_id_or_name(self, id_or_name):
        self.driver.switch_to.frame(id_or_name)

    # 思路三：
    def switch_to_frame(self, **element_dict):  # switch_to_frame(id=frameid)
        self.wait(3)
        if 'id' in element_dict.keys():
            self.driver.switch_to_frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to_frame(element_dict['name'])
        if 'element' in element_dict.keys():
            element = self.find_element(element_dict['element'])
            self.driver.switch_to_frame(element)

    # 弹出窗的封装
    def switch_to_alert(self, action='accept', time_out=local_config.time_out):
        WebDriverWait(self.driver, time_out).until(EC.alert_is_present())
        alter = self.driver.switch_to.alert
        alter_text = alter.text
        if action == 'accept':
            alter.accept()
        elif action == 'dismiss':
            alter.dismiss()
        return alter_text

    def get_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_window_by_title(self, title):
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window(window_handle)
                break

    def switch_to_window_by_url(self, url):
        window_handles = self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver, local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    def screenshot_as_file(self, *screenshot_path):
        current_dir = os.path.dirname(__file__)
        if len(screenshot_path) == 0:
            screenshot_filepath = local_config.screenshot_path
        else:
            screenshot_filepath = screenshot_path[0]
        now = time.strftime('%Y_%m_%d_%H_%M_%S')
        screenshot_filepath = os.path.join(current_dir,'..', screenshot_filepath, 'UITest_%s.png' % now)
        self.driver.get_screenshot_as_file(screenshot_filepath)


if __name__ == '__main__':
    base_page = BasePage(Browser().get_driver())
    base_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')