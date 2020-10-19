主要是实现网站的自动登录已经信息填写提交  

弹出新窗口、从数据集加载一定要考虑加载时间  
并不是没有作用而是太快了应该加个time  
滑动条为了视觉效果，要记得加sleep，如果界面没加载好，无法滑动  
用键盘模拟了滑动键  
最万能的元素查找方式    
ceshi = driver.find_element_by_xpath("//div[@class='ts_layout']//i[1]")  
https://www.cnblogs.com/minieye/p/5803640.html  
代表寻找一个class是ts_layout的div标签，然后从这里往下找到你第一个i标签  
不能向文本框中写入 有时候需要clear一下  
https://blog.csdn.net/qq_41397201/article/details/90045421  
不同的frame的元素查不到、要切换driver.switch_to.frame("right_container")  
class查找时有空格用.代替空格     官方文档      
https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/  
https://www.cnblogs.com/who-care/p/7908703.html  
主要是体力话 网页的框架（开发者模式）对流程的控制 sleep 网速 数据库查询等待  
