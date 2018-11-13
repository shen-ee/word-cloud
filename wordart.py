# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

import tokenization

txt_file = "raw.txt"
input_txt = tokenization.tokenize(txt_file)
# input_txt = "哈哈哈"

driver=webdriver.Safari()
driver.maximize_window()
driver.get(r'https://wordart.com/create')
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div/div[3]")))
fonts = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div[3]")
fonts.click()

# wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[38]/div[1]/img")))

filter = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div[3]/div[2]/div/div/input")
filter.send_keys("chinese")

chinese_fonts = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div[3]/div[2]/div/ul/li[38]/div[1]")
chinese_fonts.click()

words = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div[1]/div[1]")
words.click()

import_button = driver.find_element_by_xpath("/html/body/div/div/div/div//div/div/div/div/span/button[1]")
import_button.click()

import_area = driver.find_element_by_xpath("/html/body/div/div/div/div//div/div/div/textarea[1]")
import_area.send_keys(unicode(input_txt,'utf-8'))

import_words = driver.find_element_by_xpath("/html/body/div/div/div/div//div/div/button[@type='button'][@class='btn btn-dark']")
import_words.click()

# wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[1]/button[1]")))
# time.sleep(3)
visual = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div[1]/button[1]")
visual.send_keys(Keys.ENTER)


# driver.quit()

