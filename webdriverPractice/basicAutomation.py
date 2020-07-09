from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.get('https://youtube.com')

ytSearchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
ytSearchbox.send_keys('Funhaus')

ytSearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
ytSearchButton.click()


funhausDirect = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer[1]/div/div[2]/a/div[1]/ytd-channel-name/div/div/yt-formatted-string' ))
)

funhausDirect.click()
time.sleep(185)

driver.quit()