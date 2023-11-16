import os
def rename_files(directory, prefix):
    # 取得指定目錄下的所有檔案名稱
    files = os.listdir(directory)
    files.sort()  # 根據檔案名稱的排序

    # 依序修改檔案名稱
    for i, file_name in enumerate(files):
        # 檢查是否為檔案
        if os.path.isfile(os.path.join(directory, file_name)):
            # 新的檔案名稱
            new_file_name = f"{prefix}_{i+1:03d}.mp4"  # 修改檔案副檔名和格式

            # 修改檔案名稱
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))

# 指定目錄和前綴字元
directory = r'C:\Users\USER\Desktop\新增資料夾'
prefix = '蘇有老師上課'

# 執行檔案名稱修改
rename_files(directory, prefix)