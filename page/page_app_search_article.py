from base.base_app import BaseApp
import page

class PageAppSearchArticle(BaseApp):
    # 查找频道
    def page_search_channel(self, click_text):
        self.base_app_swipe_right_left(page.app_chanel_area, click_text)

    # 查找文章
    def page_search_article(self, click_text):
        self.base_app_swipe_down_up(page.app_article_area, click_text)

    # 组合业务方法
    def page_article(self, click_channel, click_article):
        self.page_search_channel(click_channel)
        self.page_search_article(click_article)
