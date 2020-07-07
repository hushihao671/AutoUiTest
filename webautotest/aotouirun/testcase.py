from selenium import webdriver
from webautotest.baiduweb.baidushouye import *
from webautotest.operation.baiduweb import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time


class AutoRun(unittest.TestCase):

    def setUp(self):
        OperationClass.openweb(self, "http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        """百度搜索验证"""
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(BaiduElemnt.SOUSUOKUANG))
        OperationClass.input(self, BaiduElemnt.SOUSUOKUANG, "python")
        self.isfind = OperationClass.findElement(self, BaiduElemnt.SHOUYEWHECHA)
        self.assertFalse(self.isfind, "FAIL：用例执行失败，页面元素未消失")
        OperationClass.click(self, BaiduElemnt.BAIDUBUTTON)
        OperationClass.slidingWindow(self, 0, 1000)

    def test_02(self):
        """百度首页新闻快捷按钮验证"""
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(BaiduElemnt.NEW))
        self.driver.find_element(*BaiduElemnt.NEW).click()
        self.windows = self.driver.window_handles
        self.driver.switch_to.window(self.windows[-1])
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(BaiduElemnt.RENEW), "等待新闻网页中百度按钮元素超时")
        self.title = self.driver.find_element(*BaiduElemnt.RENEW).text
        self.assertEqual("热点要闻", self.title, "用例失败：百度新闻网页的标题与实际展示结果不符")


if __name__ == '__main__':
    unittest.main()
