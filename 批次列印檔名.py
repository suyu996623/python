'''
請將/path/to/directory替換為要列出文件的目錄的實際路徑，
將/path/to/output.txt替換為保存輸出文件的實際路徑。
程序將遞歸地遍歷指定目錄及其子目錄，並將文件名寫入輸出文件中，每個文件名佔據一行。

請確保在運行此程序之前安裝了Python，
並將操作系統的路徑分隔符（在Windows上為\，在Linux或Mac上為/）正確地用於指定目錄路徑。
'''

import os

def list_files(directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory): # 走房間
            for filename in files:  # 看這個房間的檔案
                f.write(os.path.join(root, filename) + '\n')

# 指定目录路径
directory_path = r'C:\Users\USER\Desktop\python'

# 指定输出文件路径
output_file_path = r'C:\Users\USER\Desktop\新增資料夾\output.txt'

# 调用函数生成文件列表
list_files(directory_path, output_file_path)

