from selenium import webdriver
browser=webdriver.Chrome()
print(type(browser))
browser.get('http://www.baidu.com')
