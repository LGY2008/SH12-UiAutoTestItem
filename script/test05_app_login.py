import sys
import os

sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.get_dirver import GetDriver
from tool.get_log import GetLog
import pytest

log = GetLog.get_log()


class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取PageAppLogin对象
        self.login = PageIn(driver).page_get_appLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone,pwd", read_yaml("app_login.yaml"))
    def test_app_login(self, phone, pwd):
        # 调用登录业务方法
        self.login.page_app_login(phone, pwd)
        try:
            # 断言 是否登录成功
            assert self.login.page_is_login_success()
        except Exception as e:
            # 截图
            self.login.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise
