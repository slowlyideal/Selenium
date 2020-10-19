name = "显微共焦激光拉曼光谱仪"
date = 2

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
#driver.get("http://analysis.hfut.edu.cn/customer/index/index.html")
driver.get("http://ids1.hfut.edu.cn/amserver/UI/Login?goto=http://analysis.hfut.edu.cn/jzlogin.aspx")
driver.maximize_window()

#登陆
from selenium.webdriver.common.action_chains import ActionChains
login = driver.find_element_by_id("IDToken1")
login.click()
ActionChains(driver).send_keys('用户名').perform()
login_mm = driver.find_element_by_id("密码")
login_mm.click()
ActionChains(driver).send_keys('yx259142491147').perform()
ActionChains(driver).send_keys('\n').perform()

#仪器设备
yqsb = driver.find_element_by_id("i_5")
yqsb.click()



#搜索设备http://www.51testing.com/html/87/300987-831171.html
driver.switch_to.frame("right_container")
yqsb_s = driver.find_element_by_id("devname")
yqsb_s.click()
ActionChains(driver).send_keys(name).perform()
ActionChains(driver).send_keys("\n").perform()
#送样检测 从数据库查询需要时间
import time 
time.sleep(1)
# yqsb_sc = driver.find_element_by_class_name("btn_compoment")
# yqsb_sc.click()
yqsb_sc = driver.find_element_by_xpath("//ul[1]//div[1]//span[3]")
yqsb_sc.click()

#滚动条
from selenium.webdriver.common.keys import Keys 
#driver.send_keys(Keys.PageDown)
#键盘滚动
time.sleep(2)
for i in range(5):
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
  
#driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部

 
#确认界面layui-layer-btn0
time.sleep(4)
driver.switch_to.frame("Iframe1")
qr = driver.find_element_by_class_name("layui-layer-btn0")
qr.click()

#选择日期onclick="gourlsy('2020-09-28')"
from selenium.webdriver.common.by import By
rq = driver.find_element(By.XPATH,"//td[@class='kf']["+str(date)+"]")
rq.click()




#预约时段layui-layer-setwin
time.sleep(2)
sd = driver.find_element_by_link_text("选择")
sd.click()

xs = driver.find_element_by_class_name("zc")
xs.click()
close = driver.find_element_by_class_name("layui-layer-setwin")
close = driver.find_element_by_xpath("//a[@href='javascript:;']")
close.click()

#滚动条

# #driver.send_keys(Keys.PageDown)
# for i in range(5):
#     ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

#添加测试项目
time.sleep(1) #降低速度
ceshi = driver.find_element_by_xpath("//div[@class='layui-form-item']//button[1]")
ceshi.click()

ceshi = driver.find_element_by_xpath("//input[@name='ypmc']")
ceshi.clear()
ceshi.click()
ceshi.send_keys('第一杯奶茶')

time.sleep(1) #降低速度
ceshi = driver.find_element_by_id("YPS")
ceshi.click()
ActionChains(driver).send_keys('1').perform() 

time.sleep(1) #降低速度
ceshi = driver.find_element_by_xpath("//div[@class='ts_layout']//i[1]")
ceshi.click()

ceshi = driver.find_element_by_xpath("//div[@style='text-align:center']//button[1]")
ceshi.click()

time.sleep(2)
#ceshi = driver.find_element_by_xpath("//div[@id='layui-layer100005']//a[2]")
#driver.switch_to_default_content()
ceshi = driver.find_element_by_class_name("layui-layer-btn1")
ceshi.click()


for i in range(13):
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()



# 弹出新窗口、从数据集加载一定要考虑加载时间
# 并不是没有作用而是太快了应该加个time
# 滑动条为了视觉效果，要记得加sleep，如果界面没加载好，无法滑动
# 用键盘模拟了滑动键
# 最万能的元素查找方式  
# ceshi = driver.find_element_by_xpath("//div[@class='ts_layout']//i[1]")
# https://www.cnblogs.com/minieye/p/5803640.html
# 代表寻找一个class是ts_layout的div标签，然后从这里往下找到你第一个i标签
# 不能向文本框中写入 有时候需要clear一下
# https://blog.csdn.net/qq_41397201/article/details/90045421
# 不同的frame的元素查不到、要切换driver.switch_to.frame("right_container")
# class查找时有空格用.代替空格    
# 官方文档    
# https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/
# https://www.cnblogs.com/who-care/p/7908703.html
# 主要是体力话 网页的框架（开发者模式）对流程的控制 sleep 网速 数据库查询等待