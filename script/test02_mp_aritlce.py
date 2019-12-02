import sys, os

import pytest

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
import page
from page.page_in import PageIn
from tool.get_dirver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 获取PageIn对象
        self.pageIn = PageIn(driver)
        # 调用登录
        self.pageIn.page_get_mpLogin().page_login_success()
        # 获取PageMpArticlePublish对象
        self.article = self.pageIn.page_get_articlePublish()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 测试方法
    @pytest.mark.parametrize("title,content,result", read_yaml("mp_article.yaml"))
    def test_article(self, title, content, result):
        page.article_title = title
        # 调用发布文章业务方法
        self.article.page_article(title, content)
        try:
            # 断言发布结果
            assert result == self.article.page_get_add_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise
