# test script for selenium
# 1. access to google.com
# 2. search "mediee"
# 3. get the search result
# 4. save the result to csv file

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import csv
import time

driver = webdriver.Remote(
    command_executor = os.environ["SELENIUM_URL"],
    options = webdriver.ChromeOptions()
)

# 1. access to google.com
print('access to google.com')
driver.get('https://google.com')
time.sleep(3)

# 2. search "mediee"
print('search "mediee"')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('mediee')
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# 3. get the search result
print('get the search result')
search_results = driver.find_elements(By.CLASS_NAME, 'g')
results = []
for result in search_results:
    title = result.find_element(By.CLASS_NAME, 'LC20lb').text
    link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
    results.append([title, link])

# 4. create the csv file and save the result to ../data/mediee.csv
print('save the result to ../data/mediee.csv')
with open('../data/mediee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'link'])
    writer.writerows(results)


driver.quit()