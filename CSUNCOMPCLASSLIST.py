from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://mynorthridge.csun.edu/psp/PANRPRD/EMPLOYEE/SA/c/NR_SSS_COMMON_MENU.NR_SSS_SOC_BASIC_C.GBL?')

driver.implicitly_wait(25)

driver.switch_to.default_content();

driver.switch_to.frame(driver.find_element_by_id('ptifrmtgtframe'))


subject_drop_down_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'NR_SSS_SOC_NWRK_SUBJECT')))

subject_drop_down_element = Select(subject_drop_down_element)

subject = "COMP"

subject_drop_down_element.select_by_value(subject)

driver.implicitly_wait(15)

#driver.switch_to.default_content();

#driver.switch_to.frame(driver.find_element_by_id('ptifrmtgtframe'))

quick_search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,'NR_SSS_SOC_NWRK_BASIC_SEARCH_PB')))

quick_search.click()
quick_search.click()
quick_search.click()
quick_search.click()