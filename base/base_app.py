from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from base.base import Base


class BaseApp(Base):
    # 判断元素是否存在
    def base_app_element_exists(self, loc):
        try:
            self.base_find(loc, timeout=3)
            return True  # 存在
        except:
            return False  # 不存在

    # 指定区域拖拽 从右向左拽
    def base_app_swipe_right_left(self, area_loc, click_text):
        # 查找区域元素
        area_loc = self.base_find(area_loc)
        # 获取区域元素的 位置
        x = area_loc.location.get("x")
        y = area_loc.location.get("y")
        print("x:", x)
        print("y:", y)
        # 获取区域元素的 宽高
        width = area_loc.size.get("width")
        height = area_loc.size.get("height")
        print("width:", width)
        print("height:", height)
        # 计算 start_x start_y end_x end_y
        start_x = x + width * 0.8
        start_y = y + height * 0.5
        end_x = x + width * 0.2
        end_y = y + height * 0.5
        # 获取当前页面元素结构 -> 判断滑动后屏幕是否有变化使用
        page_source = self.driver.page_source
        # 组合 点击文本的元素 定位信息
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(click_text)

        # 循环
        while True:
            try:
                # 查找 点击文本 元素
                self.base_find(loc, timeout=2).click()
                print("找到了到频道了！")
                break
            except:
                # 滑动 屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 3000)

            # 判断 是否为最后一页
            if page_source == self.driver.page_source:
                print("未找到，最后一页啦！")
                # 抛异常 元素未找到！
                raise NoSuchElementException
            else:
                # 更新页面结构
                page_source = self.driver.page_source

    # 指定区域拖拽 从下到上
    def base_app_swipe_down_up(self, area_loc, click_text):
        # 查找区域元素
        area_loc = self.base_find(area_loc)
        # 获取区域元素的 宽高
        width = area_loc.size.get("width")
        height = area_loc.size.get("height")
        print("width:", width)
        print("height:", height)
        # 计算 start_x start_y end_x end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        # 获取当前页面元素结构 -> 判断滑动后屏幕是否有变化使用
        page_source = self.driver.page_source
        # 组合 点击文本的元素 定位信息
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(click_text)

        # 循环
        while True:
            try:
                # 查找 点击文本 元素
                self.base_find(loc, timeout=2).click()
                print("找到了到:{}文章！".format(loc))
                break
            except:
                # 滑动 屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 3000)

            # 判断 是否为最后一页
            if page_source == self.driver.page_source:
                print("未找到，最后一页啦！")
                # 抛异常 元素未找到！
                raise NoSuchElementException
            else:
                # 更新页面结构
                page_source = self.driver.page_source
