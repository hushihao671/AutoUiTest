from selenium import webdriver
from webautotest.baiduweb.baidushouye import *
import unittest, time


class OperationClass:

    # 打开网站
    def openweb(self, url):
        """
        :param url: 登录的地址
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()  # 浏览器窗口最大化
        self.driver.implicitly_wait(20)  # 设置隐式等待20秒

    # 输入搜索内容
    def input(self, element, content):
        """
        :param element: 页面元素
        :param content: 输入搜索的内容
        :return:
        """

        self.driver.find_element(*element).send_keys(content)

    # 点击操作
    def click(self, element):
        """
        :param element: 页面元素
        :return:
        """

        self.driver.find_element(*element).click()

    # 滑动浏览器窗口
    def slidingWindow(self, xnum: int, ynum: int):
        """
        :param xnum: 向右滑动距离
        :param ynum: 向下滑动距离
        :return:
        """

        self.driver.execute_script("window.scrollBy(" + str(xnum) + "," + str(ynum) + ")")

    def findElement(self, element):
        """
        :param element: 页面元素
        :return: true/false
        """

        find = True
        try:
            self.driver.find_element(*element)

        except:
            find = False

        finally:
            return find


if __name__ == "__main__":
    OperationClass.slidingWindow(0, 1000)
