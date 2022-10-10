# 測試網路連線
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)  # 將JSON格式資料轉換成Python資料
# ===到這裡已可印出JSON資料===

# 取得資料 (景點名稱stitle,區域address,經度longitude,緯度latitude,第一張圖檔網址file)
hwlist = data["result"]["results"]  # JSON列表層次 homework list
# a=append +=覆蓋原本的檔案
with open("data.csv", "a", encoding="utf-8-sig", newline="") as file:
    file.write ("景點,區域,經度,緯度,圖檔網址\n")
    for i in hwlist:
        if int(i["xpostDate"][0:4]) >= 2015:
            addr = i["address"][5:8]
            file2 = i["file"].split("https")
            file3 = "https" + file2[1]

            file.write(i['stitle']+',' + addr + ','+i['longitude'] + ','+i['latitude']+','+file3+"\n")
