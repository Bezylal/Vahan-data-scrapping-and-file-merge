import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException


driver = webdriver.Chrome()
url = "https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml"
driver.get(url)

for state_no in [1, 8, 15, 16, 19, 30, 31]:
    print('state no', state_no+1)
    driver.find_element("xpath",'//*[@id="j_idt41_label"]').click()
    time.sleep(0.5)
    driver.find_element("xpath",f'//*[@id="j_idt41_{state_no+1}"]').click()
    time.sleep(1)
    #navigation to set the base
    driver.find_element("xpath",'//*[@id="xaxisVar_label"]').click()
    time.sleep(0.5)
    driver.find_element("xpath",'//*[@id="xaxisVar_2"]').click()
    time.sleep(0.5)
    print('state_no', state_no)
    
    for year_no in [1,2,3,4,5,6,7,8]:
        print('year no', year_no+1)
        driver.find_element("xpath",'//*[@id="selectedYear_label"]').click()
        time.sleep(0.5)
        driver.find_element("xpath",f'//*[@id="selectedYear_{year_no+1}"]').click()
        time.sleep(0.5)
        driver.find_element("xpath",'//*[@id="j_idt71"]/span[2]').click()
        time.sleep(1)
        driver.find_element("xpath",'//*[@id="groupingTable:j_idt86"]').click()
        print('year_no', year_no)
    

    

# #Refresh
# driver.find_element("xpath",'//*[@id="j_idt68"]/span[2]').click()
# time.sleep(3)


# #to select the state & month
# for year_no in range(1, 25):
#     print('year number ', year_no+1)

# #Year
#     driver.find_element("xpath",'//*[@id="selectedYear_label"]').click()
#     time.sleep(2)
#     driver.find_element("xpath",f'//*[@id="selectedYear_{year_no+1}"]').click()
#     time.sleep(2)
#     driver.find_element("xpath",'//*[@id="j_idt68"]/span[2]').click()
#     time.sleep(2)
#     print('state clicked')

#     driver.find_element("xpath",'//*[@id="groupingTable:j_idt82"]').click()
#     time.sleep(1)
