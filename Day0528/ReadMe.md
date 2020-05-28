這周上課內容
=
[Gibbs采样](https://blog.csdn.net/google19890102/article/details/51755245?fbclid=IwAR2kFv2RSVX4qw1aERMT0-Kl5kPOvSTWY7N5iB6cagqSxTrgdSRFCDAWZ0k)

[馬爾可夫鏈蒙特卡羅算法](https://wangcc.me/LSHTMlearningnote/MCMC-methods.html?fbclid=IwAR1IuHZwxjNsjlUvF4cQnUqgRcTQt-jOG-PrdkNC4hjUhjKYpBR1HWTstic)

[吉布斯採樣](https://zh.wikipedia.org/zh-tw/%E5%90%89%E5%B8%83%E6%96%AF%E9%87%87%E6%A0%B7?fbclid=IwAR1fBoFx6Lin8knEO1dMpL8KZWba6HMEXrMA468RwHdvWpACGVOLoUiaHOo0)

蒙地卡羅方法
-
>[參考圖片](https://zh.wikipedia.org/wiki/%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85%E6%96%B9%E6%B3%95?fbclid=IwAR0dBjNEhOJAOGkBTlXoAMDL0rOjhvOPjb0SiP8LtWUepCtCRZdxOkAneyk#/media/File:Pi_30K.gif)
一類是所求解的問題本身具有內在的隨機性，藉助電腦的運算能力可以直接類比這種隨機的過程。
另一種類型是所求解問題可以轉化為某種隨機分布的特徵數，比如隨機事件出現的機率，或者隨機變數的期望值。
>>上課時我們寫道:
蒙地卡羅方法可用於近似計算圓周率：讓電腦每次隨機生成兩個0到1之間的數，看以這兩個實數為橫縱坐標的點是否在單位圓內。生成一系列隨機點，統計單位圓內的點數與總點數，（圓面積和正方形面積之比為PI:4，PI為圓周率），當隨機點取得越多時，其結果越接近於圓周率（然而準確度仍有爭議：即使取10的9次方個隨機點時，其結果也僅在前4位元與圓周率吻合[來源請求]）。用蒙地卡羅方法近似計算圓周率的先天不足是：第一，電腦產生的亂數是受到儲存格式的限制的，是離散的，並不能產生連續的任意實數；上述做法將平面分割成一個個網格，在空間也不是連續的，由此計算出來的面積當然與圓或多或少有差距。

