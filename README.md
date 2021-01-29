# cakeresume_parser

## 專案目的
這個專案主要的目的，是為了能更廣泛地瞭解不同的產業類別與公司，以及更深入地挖掘自己有興趣的公司。因此希望透過 Python 的爬蟲技巧，來快速理解不同公司的業務與核心價值，並將有興趣的公司作為進一步理解的基礎，進一步進行研究與訪談。

## 爬蟲的目標網站
因為目前鎖定的公司多數是以科技和新創公司為主，因此以比例較高的兩個求職平台 Cakeresume 和 Yourator 作為爬蟲的目標。目的是為了爬下公司的：
1. 公司名稱
2. 公司簡介
3. 公司網址

下一步會以個別感興趣的公司頁面作為爬蟲的標準，來爬取他們的需求。可能應用的技術會有 NLP 的斷詞，來進行進一步的統計與視覺化呈現。

## 使用技術
主要使用的技術有三個：
1. Beautifulsoup 4
2. Resquest
3. Selenium

針對網站的資料爬取，Cakeresume 主要使用 Request，因為網站並不像 Yourator 一樣是 Ajax 的異步加載，且網站前端並無提供 API 來直接抓取資料，所以可以直接以 Requests 的套件來直接讀取網站框架。
而針對 Yourator，則必須等網站讀取完後端資料後，再行爬取上面的介紹。

對於個別資料抓下整包的 HTML 後，較難爬取的是 Cakereume 的頁面，因為 Cakeresume 放了很多公司的說明到 Tags 裡，導致頁面的架構非常非常地混亂，且看過有經過刻意的擷取，因此這些資料很難直接被取用。僅能從頁面的介紹來抓取資料。而 Yourator 則有 Ajax 的異步加載問題，因此採用 Selenium 來模擬使用者讀取頁面，之後再從網頁中下載整包 HTML。

至於解析方式則皆以「HTML.parser」來進行解析，之後皆以 Beautifulsoup 4」來整理搜尋 elements，並結合 Pandas 來進行資料的 ETL，最後輸出成 CSV 檔以供直接參考。

## 後續資料使用方式
後續將資料放上 Google sheet 作為瀏覽與篩選的表格，並篩選出有興趣的公司，再以 LinkedIn 進行進一步地訪談與瞭解公司。

