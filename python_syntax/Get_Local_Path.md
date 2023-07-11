# CommonSyntax
### 這是一個用來記錄我常用語法的空間，會有各式語言的範例。
### 一些特殊用法也會特別做紀錄。

## 下面是範例
### 取得當前執行的python檔案的目錄
``` python
import os
# 獲取當前執行的python文件的絕對路徑
current_file_path = os.path.abspath(__file__)
# 獲取當前執行的python文件的所在目錄
current_directory = os.path.dirname(current_file_path)
print(current_directory)
```

### 以上可以取得python file 的位置後再拿到當前資料夾的位置
### 也可以用以下方法直接拿到資料夾位置
### 此為python執行的位置，非檔案所在位置
``` python
current_directory = os.getcwd() 
#這個是python執行的位置，非檔案所在位置
print(current_directory)
```
### 獲取當前Python環境目錄&Python 執行版本
``` python
import sys
import os

python_env_directory = sys.prefix
print("當前Python環境目錄：", python_env_directory)

python_version = sys.version
print("Python 執行版本：", python_version)
```