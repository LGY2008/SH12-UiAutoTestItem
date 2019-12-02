from time import sleep

from base.base import Base
import page


class PageMpArticlePublish(Base):
    # 点击内容管理
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    # 输入文章标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入文章内容
    def page_input_content(self, content):
        # 切换iframe框架
        el = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(el)
        self.base_input(page.mp_article_content, content)
        # 回到默认目录
        self.driver.switch_to.default_content()

    # 选择封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # # 选择频道
    # def page_click_channel(self):
    #     # 点击请选择
    #     self.base_click(page.mp_channel_select)
    #     sleep(2)
    #     # 选择数据库
    #     self.base_click(page.mp_channel)

    # 点击发布
    # 选择频道
    def page_click_channel(self, view_text="请选择", click_text=page.channel):
        self.base_click_ul_li(view_text, click_text)

    def page_click_publish(self):
        self.base_click(page.mp_publish_btn)

    # 获取新增结果 ->文章新增成功
    def page_get_add_result(self):
        return self.base_get_text(page.mp_publish_result)

    # 组合业务方法
    def page_article(self, title, content):
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_publish()
