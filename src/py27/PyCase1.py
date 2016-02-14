'''
Created on 2016-2-14

@author: inspur
'''
#-*- coding:utf-8 -*-

from selenium import webdriver

import time

if __name__ == "__main__":
        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")
        driver.implicitly_wait(20)
        
        driver.find_element_by_id('kw').send_keys(u'baidu')
        driver.find_element_by_id('su').click()
        
        time.sleep(20)
        
        
        driver.quit()
