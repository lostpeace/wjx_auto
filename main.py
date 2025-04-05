from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def submit_form():
    # 修改这里：填写你真实的问卷星链接
    WJX_URL = 'https://www.wjx.cn/vm/你的短id.aspx'

    # 修改这里：你的单选题题号及对应选项数量（题号:选项数）
    single_choice_questions = {
        1: 4,
        2: 3,
        3: 5,
        4: 5,
        5: 5,

    }

    # 修改这里：你的多选题题号及对应选项数量（题号:选项数）
    multiple_choice_questions = {
        6: 7,
        7: 7,
        8:4,
        9:5,
        10: 5,
        11: 6,
    }

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(WJX_URL)


    # 自动填写单选题
    for q, options in single_choice_questions.items():
        chosen_option = random.randint(1, options)
        driver.find_element(By.CSS_SELECTOR, f'[for="q{q}_{chosen_option}"]').click()
        time.sleep(random.uniform(0.3, 0.7))

    # 自动填写多选题
    for q, options in multiple_choice_questions.items():
        chosen_options = random.sample(range(1, options + 1), random.randint(1, options - 1))
        for opt in chosen_options:
            driver.find_element(By.CSS_SELECTOR, f'[for="q{q}_{opt}"]').click()
            time.sleep(random.uniform(0.2, 0.5))



    # 提交问卷
    submit_btn = driver.find_element(By.ID, 'ctlNext')
    ActionChains(driver).move_to_element(submit_btn).click().perform()

    time.sleep(2)  # 等待提交完成
    driver.quit()

    print("✅ 自动填写成功！")

for i in range(50):
    submit_form()
