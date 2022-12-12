# NKUST-Selenium-for-MacOS
---
## 目的
```
[目標]:             這是一個自動登入NKUST校務系統並可利用Line Notify通知登入成功的program,
[使用情境]:          適合在開學時校務系統異常 需要重複登入第一時間搶到停車證的碩士生使用(可從程式碼調整迴圈次數)
```
## Demo[執行畫面(YT)]:
* https://www.youtube.com/watch?v=B88ZhaFCKgI&feature=youtu.be
---
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/圖片/NKUST校務系統截圖.png)
---
## _我的Python版本: 3.9.13_
---
* _Installation_
  * cv2更新
  * time
  * selenium
  * PIL
  * ddddocr
  * requests(登入成功時利用LineNotify通知)
---
# Usage
---
## 輸入學號、密碼->執行
### step.1
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/圖片/SeleniumNKUST-Step1.png)
### step.2
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/圖片/SeleniumNKUST-Step2.png)
---
### 原理:
```
[1] 設定學號與密碼
[2] 登入校務系統頁面
[3] 截圖
[4] 定位截圖中的驗證碼位置
[5] ddddocr辨識驗證碼
[6] 輸入學號、密碼、驗證碼
[7] 點擊(click)進入頁面
[8] 若失敗(網頁異常/驗證碼辨識失敗,再次執行直到設定的迴圈次數
```
---
### 由於Mac顯示器與Windows顯示器有差別,所以要調整參數如下圖,請參考以下連結:
### _*Mac version*_
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/圖片/不同系統需調整參數.png)
---
### _*Windows顯示器設定*_
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/圖片/windows設定.png)
---
* Windows顯示器設定: https://blog.csdn.net/m0_54634272/article/details/119182147
* 截圖: https://justcode.ikeepstudying.com/2019/12/python-selenium获取验证码-selenium-webdriver-登录验证码的处理-selenium获取验/
* driver - 設定 Chrome: https://blog.csdn.net/yutu75/article/details/115524985
---
## 聲明
```
僅用於學習和交流
程式還未完整,Windows執行會遇見調參問題
歡迎任何人參與&完善
```
---
### Email: F109156120@nkust.edu.tw



