'''
Created on 2016-2-14

@author: inspur
'''

import openFrefox

def openUrl():
    print "openUrl"
    driver = openFrefox.openFirefox()
    #driver.get("http://www.baidu.com")
    #driver.implicitly_wait(20)
    return driver
    
def corrent_login():
    print "corrent_login"
    driver = openUrl()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("").send_keys("username")
    driver.find_element_by_id("").send_keys("password")
    
    driver.find_element_by_id("").click()
    
    
    
if __name__ == "__main__":
    print "main"
    openUrl()

