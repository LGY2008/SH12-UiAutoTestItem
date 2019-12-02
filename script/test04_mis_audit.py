import sys, os

sys.path.append(os.getcwd())
import page

from page.page_in import PageIn
from tool.get_dirver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 获取PageIn对象
        self.pageIn = PageIn(driver)
        # 调用登录
        self.pageIn.page_get_misLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        self.audit = self.pageIn.page_get_misAudit()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 测试方法
    def test_mis_audit(self, title=page.article_title, channel=page.channel):
        # 审核文章业务方法
        self.audit.page_audit_article(title, channel)
        try:
            # 断言...
            assert self.audit.page_is_audit_pass(title, channel)
        except Exception as e:
            # 截图
            self.audit.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
