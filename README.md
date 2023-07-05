# common_grammar
## 這是一個用來記錄我常用語法的空間


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
``` python
current_directory = os.getcwd()
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