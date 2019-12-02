from time import sleep

from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    __driver = None
    __app_driver = None

    # 获取driver
    @classmethod
    def get_web_driver(cls, url):
        if cls.__driver is None:
            # 获取driver
            cls.__driver = webdriver.Chrome()
            # 最大化
            cls.__driver.maximize_window()
            # 打开url
            cls.__driver.get(url)
        return cls.__driver

    # 获取app driver
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            # server 启动参数
            caps = {}
            # 设备信息
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '5.1'
            caps['deviceName'] = 'CSX0217728000025'
            # app的信息 /
            caps['appPackage'] = page.appPackage
            caps['appActivity'] = page.appActivity
            # 中文
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            # 不重置应用
            caps['noReset'] = False
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        return cls.__app_driver

    # 关闭driver
    @classmethod
    def quit_web_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            # 置空
            cls.__driver = None

    # 关闭app driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(5)
    GetDriver.quit_app_driver()
