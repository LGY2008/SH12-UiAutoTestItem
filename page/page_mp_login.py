from time import sleep

import page
from base.base import Base
from tool.get_log import GetLog

log = GetLog.get_log()


class PageMpLogin(Base):
    # 输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.mp_phone, phone)

    # 输入 验证码
    def page_input_verify_code(self, code):
        self.base_input(page.mp_verify_code, code)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取 昵称
    def page_get_nickname(self):
        # 重点一定要return
        return self.base_get_text(page.mp_nickname)

    # 组合 登录业务方法
    def page_login(self, phone, code):
        log.info("正在调用自媒体登录方法，用户名：{} 密码：{}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        sleep(2)
        self.page_click_login_btn()

    # 组合 登录业务方法-给依赖登录用例使用
    def page_login_success(self, phone="13012345678", code="246810"):
        log.info("正在调用自媒体登录方法，用户名：{} 密码：{}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        sleep(2)
        self.page_click_login_btn()