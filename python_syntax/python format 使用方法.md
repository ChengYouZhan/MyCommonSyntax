在 Python 中,format() 方法可以方便的格式化字符串。它使用 {} 作為定界符,在 {} 中指定要格式化的變量。
基本語法如下:
```python
"{}".format(var) 
```
舉個例子:
``` python
>>> "Hello, {}".format("John")
> 'Hello, John'
```

如果要格式化多個變量,只需要在 {} 中指定變量索引即可:
```python
 "Hello, {0}. {1}, {0}!".format("John", "Doe")
> 'Hello, John. Doe, John!'
```

也可以使用關鍵字傳入變量:
```python 
 "Hello, {first_name}. {last_name}, {first_name}!".format(first_name="John", last_name="Doe") 
> 'Hello, John. Doe, John!'
```
format() 方法還支持類型指定,可以將變量格式化為指定類型:
- {var:d} 格式化為十進制整數
- {var:o} 格式化為八進制整數
- {var:x} 格式化為十六進制整數
- {var:f} 格式化為定點浮點數
- {var:e} 格式化為指數表示法
- {var:g} 根據值的大小決定使用 fixed-point 或 exponential 格式等等
例如:
```python
"int: {0:d}; float: {1:f}".format(10, 0.5)
> 'int: 10; float: 0.500000'

"hex: {0:x}; exp: {1:e}".format(10, 100) 
> 'hex: a; exp: 1.000000e+02'
```
format() 方法使字符串格式化更加簡單易讀。在 Python 中,推薦使用 format() 方法來格式化字符串,而不是使用 % 運算符。
format() 方法的完整文檔可以參閱:https://docs.python.org/3/library/string.html#formatstrings (已編輯)