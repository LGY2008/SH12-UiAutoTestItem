import sys, os

sys.path.append(os.getcwd())
import page
import pytest

from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_dirver import GetDriver
from tool.get_log import GetLog

log = GetLog.get_log()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 获取 PageMpLogin对象
        self.mp = PageIn(driver).page_get_mpLogin()

    # 结束
    def teardown_class(self):
        # 关闭浏览器
        GetDriver.quit_web_driver()

    # 测试方法
    @pytest.mark.parametrize("phone,code,nickname", read_yaml("mp_login.yaml"))
    def test_login(self, phone, code, nickname):
        # 调用登录业务方法
        self.mp.page_login(phone, code)
        try:
            # 断言昵称
            assert nickname == self.mp.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mp.base_get_img()
            # 抛异常
            raise
