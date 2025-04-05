from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def submit_form():
    # 自动安装并启动Chrome浏览器驱动
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 打开你的问卷星链接（短链接）
    driver.get('https://www.wjx.cn/vm/wWzoZcx.aspx')

    time.sleep(1)

    # 示例自动填写，根据你实际问题修改

    # 单选题自动填写示例（第1题）
    driver.find_element(By.CSS_SELECTOR, '[for="q1_%d"]' % random.randint(1, 4)).click()

    # 单选题自动填写示例（第2题）
    driver.find_element(By.CSS_SELECTOR, '[for="q2_%d"]' % random.randint(1, 3)).click()

    # 单选题自动填写示例（第3题）
    driver.find_element(By.CSS_SELECTOR, '[for="q3_%d"]' % random.randint(1, 5)).click()

    # 单选题自动填写示例（第4题）
    driver.find_element(By.CSS_SELECTOR, '[for="q4_%d"]' % random.randint(1, 5)).click()

    # 单选题自动填写示例（第5题）
    driver.find_element(By.CSS_SELECTOR, '[for="q5_%d"]' % random.randint(1, 5)).click()

    # 多选题自动填写示例（第6题）
    for i in random.sample(range(1, 8), random.randint(1, 3)):
        driver.find_element(By.CSS_SELECTOR, '[for="q6_%d"]' % i).click()

    # 多选题自动填写示例（第7题）
    for i in random.sample(range(1, 8), random.randint(1, 4)):
        driver.find_element(By.CSS_SELECTOR, '[for="q7_%d"]' % i).click()

    # 单选题自动填写示例（第8题）
    driver.find_element(By.CSS_SELECTOR, '[for="q8_%d"]' % random.randint(1, 4)).click()

    # 多选题自动填写示例（第9题）
    for i in random.sample(range(1, 6), random.randint(1, 3)):
        driver.find_element(By.CSS_SELECTOR, '[for="q9_%d"]' % i).click()


    # 多选题自动填写示例（第10题）
    for i in random.sample(range(1, 6), random.randint(1, 3)):
        driver.find_element(By.CSS_SELECTOR, '[for="q10_%d"]' % i).click()

    # 多选题自动填写示例（第11题）
    for i in random.sample(range(1, 7), random.randint(1, 4)):
        driver.find_element(By.CSS_SELECTOR, '[for="q11_%d"]' % i).click()

    time.sleep(1)

    # 提交按钮
    submit_btn = driver.find_element(By.ID, 'ctlNext')
    ActionChains(driver).move_to_element(submit_btn).click().perform()

    time.sleep(2)  # 等待提交完成

    print("✅ 提交成功！")

    driver.quit()

for i in range(50):
    submit_form()

