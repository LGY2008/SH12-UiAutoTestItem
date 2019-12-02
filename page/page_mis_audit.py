from time import sleep

import page
from base.base import Base


class PageMisAudit(Base):

    # 文章id
    article_id = None

    # 点击 信息管理
    def page_click_info_manage(self):
        sleep(2)
        self.base_click(page.mis_info_manage)

    # 点击 内容审核
    def page_click_content_audit(self):
        sleep(1)
        self.base_click(page.mis_content_audit)

    # 输入 文章title
    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    # 输入 频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 选择状态 -> 待审核
    def page_click_status(self, view_text="请选择状态", click_text="待审核"):
        self.base_click_ul_li(view_text, click_text)

    # 点击 查询
    def page_click_search(self):
        self.base_click(page.mis_find)

    # 获取id
    def page_get_article_id(self):
        sleep(2)
        self.article_id = self.base_get_text(page.mis_article_id)

    # 点击 通过
    def page_click_pass(self):
        self.base_click(page.mis_pass_btn)

    # 确认 修改
    def page_click_pass_confirm(self):
        self.base_click(page.mis_pass_confirm)

    # 判断是否审核通过
    def page_is_audit_pass(self, title, channel):
        sleep(3)
        # 刷新页面
        self.driver.refresh()
        # 输入title
        self.page_input_title(title)
        # 输入 频道
        self.page_input_channel(channel)
        # 选择状态 ->审核通过
        self.page_click_status(click_text="审核通过")
        # 点击查询
        self.page_click_search()
        sleep(8)
        # 判断 页面中是否包含id(单独封装方法，判断id是否存在)
        return self.base_is_exists_text_element(self.article_id)
    # 组合业务方法
    def page_audit_article(self, title, channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_search()
        self.page_get_article_id()
        print("要审核的id为：", self.article_id)
        self.page_click_pass()
        self.page_click_pass_confirm()
