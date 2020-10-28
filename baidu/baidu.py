  
#打开一个网站 并最大化
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://baidu.com")
driver.maximize_window()
