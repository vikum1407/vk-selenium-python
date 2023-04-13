from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browserName = "firefox"

if browserName == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browserName == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    print("Please pass the current browser name")

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree")
driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@id='justAnInputBox']").click()
'''
    Here I did the dropdown field validation in 3 ways:-
    
        1. Normal JQuery dropdown [method name = multi_choice_method] -
                Here we can click the choice only one
        
        2. Normal JQuery dropdown with multiple choices click [method name = muti_choice_methodwithList] -
                Here we can click only selected choices but not the all options
                
        3. Normal JQuery dropdown with multiple choices and all option click [method name = muti_Allchoice_methodwithList] -
                Here we can click single choice, multi choices and all choices


'''
def multi_choice_method(eleList, value):
    for ele in eleList:
        if ele.text == value:
            ele.click()
            break

# this is also very time-consuming thing to do over and over. So we can enhance the method as above[value get as a list]

def muti_choice_methodwithList(eleList, choices):
    for i in eleList:
        for j in range(len(choices)):
            if i.text == choices[j]:
                i.click()

def muti_Allchoice_methodwithList(eleList, choices):
    if not choices[0] == 'all':
        for i in eleList:
            for j in range(len(choices)):
                if i.text == choices[j]:
                    i.click()
    else:                           # without exception handling we can observe an error for some elements
        try:
            for ele in eleList:
                ele.click()
        except Exception as e:
            print(e)

dripList = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')

# for ele in dripList:
#     if ele.text == 'choice 2':
#         ele.click()
#         break
# multi_choice_method(dripList, 'choice 2')
# multi_choice_method(dripList, 'choice 3')
# multi_choice_method(dripList, 'choice 4')

#value_list = ['choice 2','choice 3','choice 4']
#value_list = ['choice 2']
value_list = ['all']
#muti_choice_methodwithList(dripList, value_list)
muti_Allchoice_methodwithList(dripList,value_list)



