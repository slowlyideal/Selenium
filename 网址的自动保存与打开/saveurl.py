# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:56:50 2020

@author: penghui
"""
import pyautogui as pi
#import time
import pyperclip as pp
from os import getcwd
name = pi.prompt(title='请输入txt名字(在浏览器界面下填写并点击确定)')
name_txt = 'url_'+name
#time.sleep(2)
i = 1
site_list = []
while(i>0):
    pi.moveTo(600,50,2)
    #time.sleep(3)
    pi.click(button='left')
    pi.hotkey('ctrl', 'a')
    pi.hotkey('ctrl','c')
    #获取粘贴板内容
    site = pp.paste()
    print(site)
    if site in site_list:
        break
    else:
        site_list.append(site)
        #切换tab
        pi.hotkey('ctrl', 'PgDn')
#写入到txt
#name = 'openurl'+time.strftime("%m{m}%d{d}%H:%M:%S", time.localtime()).format(m='月',d='日')

dirurl = getcwd()+'/url_'+name+'.txt'
f = open(dirurl,'w')#a
site_list_len = len(site_list)
for item in site_list:
    f.write(item+'\n')
#一定不能忘记
f.close()
pi.alert("已经将当前窗口的"+str(site_list_len)+"个标签页写入到"+name_txt+".txt")
#