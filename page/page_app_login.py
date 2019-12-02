import page

from base.base_app import BaseApp


class PageAppLogin(BaseApp):
    # 输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 点击 登录按钮
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 判断是否登录成功
    def page_is_login_success(self):
        # True 存在 False 不存在
        return self.base_app_element_exists(page.app_me)

    # 登录 业务方法
    def page_app_login(self, phone, pwd):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

   # 登录 业务方法
    def page_app_login_success(self, phone="13012345678", pwd="246810"):
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()