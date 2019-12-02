import sys, os

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
import pytest
from page.page_in import PageIn
from tool.get_dirver import GetDriver
import page
from tool.get_log import GetLog

log = GetLog.get_log()


class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 获取PageMisLogin对象
        self.mis = PageIn(driver).page_get_misLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 测试方法
    @pytest.mark.parametrize("username,pwd,nickname", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, nickname):
        # 调用登录业务方法
        self.mis.page_mis_login(username, pwd)
        try:
            # 断言昵称
            assert nickname in self.mis.page_get_nickname()
        except Exception as e:
            # 截图
            self.mis.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
