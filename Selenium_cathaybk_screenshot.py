from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

def open_web(url="https://www.cathaybk.com.tw/cathaybk/", wait_time=3): 
    options = Options()
    options.edge_executable_path = "C:/Users/Ives/Downloads/Webdriver/chromedriver.exe" #指定driver路徑
    
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1500, 1300) #設定視窗大小
    driver.get(url)
    driver.implicitly_wait(wait_time) #等待網頁loading
    
    return driver

def capture_screenshot(driver,screenshot_path):
    driver.save_screenshot(screenshot_path)

"""
def count_card_list_item(driver):
    driver.find_element(By.XPATH,"//div[text()='產品介紹']").click()
    time.sleep(1)
    div_ = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]") # xpath絕對路徑
    a_ = div_.find_elements(By.XPATH,".//a")
    return len(a_)
"""

def count_card_list_item(driver):
    driver.find_element(By.XPATH,"//div[text()='產品介紹']").click()
    time.sleep(1)
    div_ = driver.find_elements(By.XPATH,"//div[@class='cubre-o-menuLinkList__content']") #該元素共13個
    div_ = div_[1] #第2個是目標元素
    a_ = div_.find_elements(By.XPATH,".//a") #.//a 代表目標元素後面的<a>
    return len(a_)

def go_to_card_list(driver):
    driver.find_element(By.XPATH,"//div[text()='產品介紹']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[text()='卡片介紹']").click()
    time.sleep(1)

def go_to_page_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def count_unavaliable_cards(driver):
    count = driver.find_elements(By.XPATH,"//div[contains(text(),'本卡已停止申辦')]") 
    return len(count)

def unavaliable_cards_screenshot(driver):
    count = driver.find_elements(By.XPATH,"//div[contains(text(),'本卡已停止申辦')]") # 決定要按向右按鈕幾次
    next = driver.find_elements(By.XPATH,"//div[@class='cubre-o-slide__next swiper-next']") # 定位向右按鈕
    next_btn = next[3] # 網頁中第四個向右按鈕
    driver.save_screenshot("C:/Users/Ives/Downloads/screenshot3.png")
    for n in range(len(count)-3): # 總共10張卡 扣掉第一個截圖可以截到的3張
        next_btn.click()
        time.sleep(0.5)
        driver.save_screenshot("C:/Users/Ives/Downloads/screenshot"+str(n+4)+".png") 
        
driver = open_web()
print("Question1 官網首頁截圖")
capture_screenshot(driver,"C:/Users/Ives/Downloads/screenshot1.png")
print("Question2 計算信用卡列表項目並截圖")
print(count_card_list_item(driver))
capture_screenshot(driver,"C:/Users/Ives/Downloads/screenshot2.png")
driver.quit()
driver = open_web()
go_to_card_list(driver)
go_to_page_end(driver)
print("Question3 計算已停用信用卡數量並截圖")
print(count_unavaliable_cards(driver))
unavaliable_cards_screenshot(driver)
