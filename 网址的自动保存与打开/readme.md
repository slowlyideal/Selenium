运行效果见：https://www.bilibili.com/video/BV1ca411A7E2  

将浏览器的网址写入到txt并打开  
1.写入txt：  
pyautogui实现网址选取、复制、txt命名  
pyperclip实现读取剪切板  
2.读出打开：  
selenium 实现  
3.打包exe  
pyinstaller    
#https://pypi.org/project/pyperclip/  pyperclip实现读取剪切板  
#https://pyautogui.readthedocs.io/en/latest/msgbox.html pyautogui实现对鼠标和键盘d操作  
#https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/ selenium实现对浏览器的操作  
#https://pyinstaller.readthedocs.io/en/stable/usage.html  打包成exe Pyinstaller -F -w main.py 避免cmd和依赖  
