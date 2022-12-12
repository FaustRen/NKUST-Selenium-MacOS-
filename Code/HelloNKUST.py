#%%
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from PIL import Image
import ddddocr
import requests


def line_notify(message,notify_time,line_token_input):
    LINE_URL = 'https://notify-api.line.me/api/notify'
    LINE_TOKEN = line_token_input
    for _ in range(notify_time):
        requests.post(
            LINE_URL,
            headers={'Authorization': f'Bearer {LINE_TOKEN}'},
            data={'message': message})


class GoNKUST:
    
    def __init__(self, st_id, st_pwd,img_path='./screenshot_2.png',verify_code_path='./verifyCode4.png'):
        self.st_id=st_id
        self.st_pwd=st_pwd
        self.img_path=img_path
        self.verify_code_path=verify_code_path
        
        
    def setUp(self, url):
        self.chrome_options = Options()
        self.driver=webdriver.Chrome(executable_path='./chromedriver', chrome_options=self.chrome_options)
        self.driver.set_window_size(1200,851)
        self.driver.get(url)
        time.sleep(1)
        width = self.driver.execute_script("return document.documentElement.scrollWidth")# 取得長寬
        height = self.driver.execute_script("return document.documentElement.scrollHeight")
        self.driver.set_window_size(width, height)#設定長寬
        self.driver.get_screenshot_as_file(self.img_path)
        print("get screen sucessfully")
        
    def idElement(self,id_name):
        element_output = self.driver.find_element(By.ID, id_name)
        return element_output
    
    def tagElement(self, tag_name):
        tag_output = self.driver_find_element(By.TAG_NAME, tag_name)
        return tag_output

    def elementLocation(self, element_input):
        left = int(element_input.location['x'])*2
        top = int(element_input.location['y'])*2
        right = int(element_input.location['x'] + element_input.size['width'])*2
        bottom = int(element_input.location['y'] + element_input.size['height'])*2
        return left,top,right,bottom
    
    def locateImg(self,left,top,right,bottom):
        im = Image.open(self.img_path)
        im = im.crop((left, top, right, bottom))
        im = im.convert("RGB")
        im.save(self.verify_code_path)
        ## 辨識驗證碼
        ocr = ddddocr.DdddOcr()
        verify_code_res = ocr.classification(im)
        return verify_code_res
    
    def loginNKUST(self,):
        self.setUp("https://webap.nkust.edu.tw/nkust/index_main.html?1111")
        element1 = self.idElement('verifyCode')
        left_side, top_side, right_side, bottom_side=self.elementLocation(element1)
        verify_res = self.locateImg(left_side, top_side, right_side, bottom_side)
        # 帳號
        user=self.driver.find_element(By.ID, "uid")
        user.clear()
        user.send_keys(self.st_id)
        # 密碼
        pwd =self.driver.find_element(By.ID, "pwd")
        pwd.clear()
        pwd.send_keys(self.st_pwd)
        # 驗證碼
        verify_code=self.driver.find_element(By.ID, "etxt_code")
        verify_code.clear()
        verify_code.send_keys(verify_res)
        self.driver.find_element(By.XPATH, "//*[@id='chk']").click()
        time.sleep(1.5)
        driver_output = self.driver
        return driver_output
    
    def closerDriver(self):
        """driver close"""
        self.driver.close()
        
        
if __name__ == '__main__':
    學號=input("請輸入學號:")
    密碼=input("請輸入密碼:")
    
    網頁截圖='./screenshot_2.png'
    驗證碼截圖='./verifyCode4.png'
    line權杖="設定Line權杖"
    line通知次數=3
    
    # 執行
    for _ in range(5):
        try:
            goNkust = GoNKUST(學號,密碼,網頁截圖,驗證碼截圖)
            driver_res = goNkust.loginNKUST()
            if driver_res.find_elements(By.TAG_NAME, "li") is not None:
                print("Y")
                # line_notify("已登入校務系統",line通知次數,line權杖)
        
                break
        except: 
            goNkust.closerDriver()
            continue
        
    
    
    
        
    
    
    
    
        
    
    
                
        

# %%

























