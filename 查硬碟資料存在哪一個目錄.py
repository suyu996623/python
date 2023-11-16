import os
import re

lines = []

for root, dirs, files in os.walk("F:/"):

    for file in files :

        if re.match("錄製(_....){1}(_..){5}(_...){1}.mp4",file) !=  None  :
            print(file)
            if root not in lines :
                print(root)
                print('============')
                lines.append(root)
                lines.append('\n')
with open('mp4.txt', 'w',encoding="utf-8") as f:
    f.writelines(lines)
