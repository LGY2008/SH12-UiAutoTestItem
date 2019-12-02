import sys
import os

sys.path.append(os.getcwd())
import pytest

from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.get_dirver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestAppArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取PageIn对象
        self.page = PageIn(driver)
        # 调用登录
        self.page.page_get_appLogin().page_app_login_success()
        # 获取PageAppSearchArticle 对象
        self.article = self.page.page_get_appSearchArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 查找文章测试方法
    @pytest.mark.parametrize("click_channel,click_article", read_yaml("app_article.yaml"))
    def test_article(self, click_channel, click_article):
        try:
            # 调用查找文章业务方法
            self.article.page_article(click_channel, click_article)
        except Exception as e:
            # 截图
            self.article.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
