from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from utils import debug

chrome_options = Options()
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('--hide-scrollbars')
# 不加载图片, 提升速度
chrome_options.add_argument('blink-settings=imagesEnabled=false')

if debug:
    driver = webdriver.Edge()
else:
    driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()


def get() -> WebDriver:
    return driver


def close():
    driver.close()
