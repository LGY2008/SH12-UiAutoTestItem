import page
from base.base import Base


class PageMisLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 重点：必须处理 登录按钮可用属性
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        self.base_click(page.mis_login_btn)

    # 获取登录后信息
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组合业务方法
    def page_mis_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合业务方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()