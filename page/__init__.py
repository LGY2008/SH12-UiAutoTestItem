from selenium.webdriver.common.by import By

from tool.read_yaml import read_yaml

"""以下为黑马头条项目url配置数据"""
# 自媒体url
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理url
url_mis = "http://ttmis.research.itcast.cn/#/"

"""以下为app配置数据"""
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity"
# 文章title
article_title = read_yaml("mp_article.yaml")[0][0]
# 频道
channel = "数据库"

"""以下为自媒体配置数据 """
# 手机号
mp_phone = By.CSS_SELECTOR, ".el-input__inner"
# 验证码
mp_verify_code = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
# 点击内容管理
mp_content_manage = By.XPATH, "//*[text()='内容管理']/.."
# 点击发布文章
mp_publish_article = By.XPATH, "//ul[@class='el-menu el-menu--inline']//*[contains(text(),'发布文章')]"
# 输入文章标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 切换iframe
mp_iframe = By.ID, "publishTinymce_ifr"
# 输入文章内容
mp_article_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[contains(text(),'自动')]/.."
# 选择频道
mp_channel_select = By.CSS_SELECTOR, "[placeholder='请选择']"
mp_channel = By.XPATH, "//ul/li/*[text()='数据库']"
# 点击发布
mp_publish_btn = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取新增结果 ->文章新增成功
mp_publish_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下为后台管理系统配置数据"""
# 用户名
mis_username = By.CSS_SELECTOR, "[placeholder='用户名']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[placeholder='密码']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取昵称
mis_nickname = By.CSS_SELECTOR, ".user_info>span"
# 信息管理
mis_info_manage = By.XPATH, "//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']"
# title
mis_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询
mis_find = By.CSS_SELECTOR, ".find"
# id
mis_article_id = By.XPATH, "//div[@class='cell']/span"
# 通过
mis_pass_btn = By.XPATH, "//*[text()='通过']/.."
# 确定修改
mis_pass_confirm = By.CSS_SELECTOR, ".el-button--primary"

"""app配置数据"""
# 手机号
app_phone = By.XPATH, "//*[@index='1' and @class='android.widget.EditText']"
# 验证码
app_pwd = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录
app_login_btn = By.XPATH, "//*[@class='android.widget.Button']"
# 我的
app_me = By.XPATH, "//*[contains(@text,'我的') and @index='3']"
# 频道区域
app_chanel_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article_area = By.XPATH, "//*[@bounds='[0,390][1080,1716]']"
