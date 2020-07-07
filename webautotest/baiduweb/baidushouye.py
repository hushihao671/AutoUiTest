from selenium.webdriver.common.by import By

"""
UI自动化页面元素集合
"""
class BaiduElemnt():
    SOUSUOKUANG = (By.XPATH, '//input[@id="kw"]')  # 百度首页搜索输入框
    GOTOSHOUYE = (By.XPATH, '//a[@id="result_logo"]/img[1]')  # 百度首页图标
    SHOUYEWHECHA = (By.XPATH,'//div[@class="qrcode-layer icon-mask-wrapper"]')  # 百度首页二维码
    BAIDUBUTTON = (By.ID,"su")  # 百度按钮
    NEW = (By.LINK_TEXT,"新闻")  # 新闻链接
    TITLE = (By.XPATH,"/html/head/title")  # 百度新闻网页标题
    RENEW = (By.XPATH,'//a[text()="热点要闻"]')  # 热点新闻
