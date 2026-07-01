import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome()
url = "https://vahan.parivahan.gov.in/vahan4dashboard/vahan/view/reportview.xhtml"
driver.get(url)
time.sleep(2)
#navigation to set the base
driver.find_element("xpath",'//*[@id="j_idt39"]/div[3]/span').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="j_idt39_32"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="yaxisVar_label"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="yaxisVar_0"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="xaxisVar_label"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="xaxisVar_2"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="selectedYear_label"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="selectedYear_1"]').click()
time.sleep(0.5)
driver.find_element("xpath",'//*[@id="j_idt70"]/span[2]').click()
time.sleep(1)
# driver.find_element("xpath",'//*[@id="j_idt36_16"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//*[@id="selectedYear_label"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//*[@id="selectedYear_1"]').click()
# time.sleep(1)
# driver.find_element("xpath",'//*[@id="j_idt66"]/span[2]').click()
# time.sleep(1)
# for year in range(9, 16):
#     driver.find_element("xpath",'//*[@id="selectedYear_label"]').click()
#     time.sleep(1)
#     driver.find_element("xpath",f'//*[@id="selectedYear_{year}"]').click()
#     time.sleep(2)

#mylist_bangalore = [7,8,9,10,11,36,24,68,27,42,62,16,65,40,39,17,53,64,50,43,20]
mylist_chennai = [4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 46, 55, 66, 89, 95, 96, 103, 112, 131, 132]
#mylist_coimbatore = [27, 28, 29, 30]
#mylist_madurai = [57, 58, 59]
##mylist_salem = [97, 98, 99]
#mylist_trichy = [126, 127]
#mylist_thirunelveli = [128]


#to select the state & month
for rto_no in mylist_chennai:
    print('rto number ', rto_no)

    driver.find_element("xpath",'//*[@id="selectedRto_label"]').click()
    time.sleep(1)
    driver.find_element("xpath",f'//*[@id="selectedRto_{rto_no}"]').click()
    time.sleep(1)
    driver.find_element("xpath",'//*[@id="j_idt70"]/span[2]').click()
    time.sleep(1)
    #driver.find_element("xpath",'//*[@id="groupingTable:j_idt81"]').click()
    #time.sleep(1)

    print('rto clicked')
    driver.find_element("xpath",'//*[@id="groupingTable:j_idt84"]').click()
    time.sleep(1)


#         for month_no in range(1, 13):
#             print('month number ', month_no)
#             try:
#                 driver.find_element("xpath",'//*[@id="groupingTable:selectMonth_label"]').click()
#                 time.sleep(1)
#                 driver.find_element("xpath",f'//*[@id="groupingTable:selectMonth_{month_no}"]').click()
#                 time.sleep(2)
#                 driver.find_element("xpath",'//*[@id="groupingTable:j_idt78"]').click()
#                 time.sleep(1)
#                 print('month number', month_no,'downloaded')
#                 time.sleep(1)
#             except NoSuchElementException:
#                 print('Element not found for month', month_no)
#                 break
