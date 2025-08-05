<h1>設計細節介紹:</h1>
註冊頁面，輸入資料後會連接至MySQL資料庫中(如圖2)</br>

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/%E5%9C%96%E7%89%87%201.png)

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/%E5%9C%96%E7%89%87%202.png)
(圖2)

<h2>情境:</h2>
1.	若帳號密碼有一重複，會轉跳至註冊失敗頁面，並且錯誤訊息會從動態網址列的Query String中取得 

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/3.png)

2.	若輸入無重複，則會出現 註冊成功!

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/4.png)

<ins>**登入頁面**</ins>，登入時後端程式接收到使用者輸入的資料，會檢查資料庫中是否有相對應的帳號、密碼。

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/5.png)

<h2>情境:</h2>
1.	有相對應的帳號、密碼
登入後會轉跳會員頁面，並帶出使用者姓名

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/6.png?raw=true) </br>

並會將資訊加入session中記錄

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/7.png?raw=true)

2.	若帳號密碼未在資料庫中，則轉跳失敗頁面。同樣錯誤訊息會從動態網址列的Query String中取得

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/8.png?raw=true)

<ins>**登出頁面:**</ins>
點擊會員頁Log out的按鍵後，會清空session中紀錄的使用者資訊，並直接導回首頁。

![image](https://github.com/joylearncode/joylearncode.github.io/blob/main/week-6/img/9.png?raw=true)

</br>
</br>
</br>
