# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:26:17 2020

@author: penghui
"""

#读取txt中的网址并打开
from selenium import webdriver
import pyautogui as pi
#import time
from os import getcwd
name = pi.prompt(title='请输入txt名字')
name_txt = 'url_'+name
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

dirurl = getcwd()+'/url_'+name+'.txt'
f = open(dirurl,'r')
count = 0
for line in f:
    line = line.split('\n')
    print(line[0])
    print("window.open('"+line[0]+"')")
    driver.execute_script("window.open('"+line[0]+"')")
    count = count+1
f.close()

# js = "window.open('http://www.sogou.com')"
# driver.execute_script(js)
import pyautogui as pi
pi.alert(name_txt+".txt的"+str(count)+"个标签页已经打开")
