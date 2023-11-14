# _*_ coding: utf-8 _*_
"""
@File       : 10_动态渲染页面爬取.py
@Author     : Tao Siyuan
@Date       : 2021/12/17
@Desc       :...
"""
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""1.Selenium的使用"""
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

"""2.声明浏览器对象"""
# browser1 = webdriver.Chrome()
# browser2 = webdriver.Edge()
# browser3 = webdriver.Firefox()
# browser5 = webdriver.Safari()

"""3.访问页面"""
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

"""4.查找节点"""
# 1. 查找单个节点 find_element
input_first = browser.find_element_by_id('q')   # 根据id值来选择
input_second = browser.find_element_by_css_selector('#q')    # 根据css选择器来选择
input_third = browser.find_element_by_xpath('//*[@id="q"]')  # 根据XPath来选择
print(input_first, input_second, input_third)
browser.close()
# 还有根据name值等许多其他属性来选择
# 返回节点为WebElement类型
input_first = browser.find_element(By.ID, 'q')  # 这种查找方式与上述一致，但是参数更灵活
# 2. 查找多个节点 find_elements
lis = browser.find_elements_by_css_selector('service-bd li')
print(lis)  # 返回为列表类型
browser.close()
# 更多选择方法见P266

"""5.节点交互"""
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# 一般的交互动作都是针对某个节点执行的，例如：输入框&按钮

"""6.动作链"""
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# # 菜鸟教程拖曳实例
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

"""7.执行JavaScript"""
# 类似下拉进度条等操作，selenium没有提供相应的API，可采取直接执行javascript进行
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

# 注意此处的JavaScript的用法

"""8.获取节点信息"""
# 1.获取属性:get_attribute()方法
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 2.获取文本值: WebElement.text属性
# browser =webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_xpath('button[@type="button" and contains["@class_", "Button--primary"]')
# print(input.text)

# 3.获取id、位置、标签名和大小
# 基于WebElement节点的属性：id，location，tag_name，size(width and height)

"""9.切换Frame"""
# # 网页的一种节点为iframe，即子Frame------页面的子页面。如果需要获取子Frame节点需要切换
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchFrameException:
#     print('No Logo!')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)




