import requests
import pandas as pd

# 設定time為獲取中文姓名100筆的倍數。time=3，就是300筆的意思。
times = 2
cnames = []
for x in range(times):
    url = 'http://www.richyli.com/name/index.asp'
    r = requests.get(url)
    r.encoding = 'big5'

    # 將網頁中的資料以分行的方式存成文字檔
    result = r.text.splitlines()

    # 114是中文姓名開始的列，找到最後一個「、」，設定成為字串的切片位置。
    char_index = result[114].rfind("、")
    temp = result[114][:char_index]

    # 將temp的100筆姓名新增到cnames中
    cnames.append(temp)

# 將每100筆姓名的list加一個「、」，再組合成字串存到my_names中
my_names = "、".join(str(x) for x in cnames)
print(my_names)