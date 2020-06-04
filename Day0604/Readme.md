巴斯卡三角形
-
楊輝三角形，又稱帕斯卡三角形、賈憲三角形、海亞姆三角形、巴斯卡三角形，是二項式係數的一種寫法，形似三角形，在中國首現於南宋楊輝的《詳解九章算法》得名，
.書中楊輝說明是引自賈憲的《釋鎖算書》，故又名賈憲三角形。前 9 行寫出來如下：

```
　　　　　　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１
```



程式部分
-
```
1.先 git clone https://github.com/ccccourse/se
2.下載NODE.JS      
3.執行一下 CnkDynamic.js
```
[NODE.JS](https://nodejs.org/en/)
![image](https://github.com/TKTim/ai108b/blob/master/Day0604/1.png)

排列組合器
-
[引導網站](http://gadget.chienwen.net/x/math/percomb?fbclid=IwAR1v93Y2ZznaTBGHnteoB2PbmjB7uJQ7Y_5LqzEm8-6U_RHa9P1DoM7kSYU)

萊文斯坦距離
-
```
萊文斯坦距離，又稱Levenshtein距離，是編輯距離的一種。指兩個字串之間，由一個轉成另一個所需的最少編輯操作次數。

允許的編輯操作包括：

1.將一個字符替換成另一個字符
2.插入一個字符
3.刪除一個字符
俄羅斯科學家弗拉基米爾·萊文斯坦在1965年提出這個概念。

應用:
DNA分析
拼寫檢查
語音辨識
抄襲偵測
```
講真的，可能還是看不懂，那就看個好懂的例子:
```
將「kitten」一字轉成「sitting」的萊文斯坦距離為3：

kitten → sitten （k→s）
sitten → sittin （e→i）
sittin → sitting （插入g）

了解後我們運行editDistance.js
```
![image](https://github.com/TKTim/ai108b/blob/master/Day0604/2.png)


遺傳演算法
-
[遺傳演算法](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95/E-%E5%AF%A6%E4%BD%9C%EF%BC%9A%E9%81%BA%E5%82%B3%E6%BC%94%E7%AE%97%E6%B3%95?fbclid=IwAR3e1CnBpiN3fMKAixvR5LCZ4yyqV3kxsrSLjE33gBD2NatSztcR-_1JhfM)










