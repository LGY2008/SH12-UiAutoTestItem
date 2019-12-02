from page.page_app_login import PageAppLogin
from page.page_app_search_article import PageAppSearchArticle
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article_publish import PageMpArticlePublish
from page.page_mp_login import PageMpLogin


class PageIn:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_mpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticlePublish对象
    def page_get_articlePublish(self):
        return PageMpArticlePublish(self.driver)

    # 获取PageMisLogin对象
    def page_get_misLogin(self):
        return PageMisLogin(self.driver)

    # 获取PageMisAudit对象
    def page_get_misAudit(self):
        return PageMisAudit(self.driver)

    # 获取PageAppLogin对象
    def page_get_appLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppSearchArticle对象
    def page_get_appSearchArticle(self):
        return PageAppSearchArticle(self.driver)