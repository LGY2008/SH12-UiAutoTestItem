from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_log import GetLog

log = GetLog.get_log()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在获取driver对象：{}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找: {} 元素".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找多个元素
    def base_finds(self, loc, timeout=30, poll=0.5):
        log.info("正在查找: {} 元素".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 输入
    def base_input(self, loc, value):
        # 获取元素
        log.info("正在调用查找元素方法")
        el = self.base_find(loc)
        log.info("正在对：{} 元素执行清空操作".format(loc))
        # 清空
        el.clear()
        log.info("正在对：{} 元素执行输入：{} 操作".format(loc, value))
        # 输入
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        log.info("正在对：{} 元素执行点击操作".format(loc))
        self.base_find(loc).click()

    # 获取 文本方法
    def base_get_text(self, loc):
        log.info("正在获取：{} 元素文本：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用将图片写入报告
        self.__base_write_report()

    # 将图片写入报告
    def __base_write_report(self):
        with open("./image/err.png", "rb") as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)

    # 点击 ul->li
    def base_click_ul_li(self, view_text, click_text):
        sleep(1)
        # 组合显示文本 loc
        loc = By.XPATH, "//*[@placeholder='{}']".format(view_text)
        # 查找显示文本元素，并点击
        self.base_find(loc).click()
        sleep(2)
        # 查找一组元素 li
        loc = By.CSS_SELECTOR, "ul>li"
        els = self.base_finds(loc)
        for el in els:
            # 如果遍历当前的li元素文本和 click_text相同
            if el.text == click_text:
                el.click()
                break

    # 判断 页面是否包含指定文本串的 元素
    def base_is_exists_text_element(self, text):
        loc = By.XPATH, "//*[contains(text(),'{}')]".format(text)
        try:
            self.base_find(loc, timeout=5)
            print("找到啦！，找到包含文本：{} 的元素".format(text))
            return True  # 元素存在
        except:
            return False  # 元素不存在
