# NKUST-Selenium-for-MacOS
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/NKUST校務系統截圖.png)
---
## _我的Python版本: 3.9.13_
---
* 套件
  * selenium
  * PIL
  * ddddocr
  * requests(登入成功時利用LineNotify通知)
---
## 輸入學號、密碼->執行
### step.1
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/SeleniumNKUST-Step1.png)
### step.2
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/SeleniumNKUST-Step2.png)
---
```
###原理:
[1]設定學號與密碼
[2]登入校務系統頁面
[3]截圖
[4]定位截圖中的驗證碼位置
[5]ddddocr辨識驗證碼
[6]輸入學號、密碼、驗證碼
[7]點擊(click)進入頁面
```
---
### 由於Mac顯示器與Windows顯示器有差別,所以要調整參數如下圖,請參考以下連結:
![GITHUB](https://github.com/FaustRen/NKUST-Selenium-MacOS-/blob/main/不同系統需調整參數.png)
---
* Windows顯示器設定: https://blog.csdn.net/m0_54634272/article/details/119182147
* 截圖: https://justcode.ikeepstudying.com/2019/12/python-selenium获取验证码-selenium-webdriver-登录验证码的处理-selenium获取验/
* driver - 設定 Chrome: https://blog.csdn.net/yutu75/article/details/115524985
---
