# Python 檔案操作練習

這份指南搭配 `readfile.py` 和 `sample.txt` 使用，帶你一步一步認識 Python 如何讀取與寫入文字檔。

## 開始前

確認這三個檔案放在同一個資料夾：

- `readfile.md`：本操作指南
- `readfile.py`：練習程式
- `sample.txt`：提供給程式讀取的範例文字

在終端機切換到這個資料夾，執行：

```powershell
python readfile.py
```

## 練習一：讀取整個檔案

```python
with sample_file.open("r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

- `"r"` 表示讀取模式。
- `read()` 會讀取整個檔案的內容。
- `encoding="utf-8"` 可正確處理中文。
- `with` 區塊結束時會自動關閉檔案。

可以先打開 `sample.txt` 看看內容，再觀察程式印出的結果。

## 練習二：逐行讀取

```python
with sample_file.open("r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

這個 `for` 迴圈每次讀取一行。`print` 預設會在文字後加上換行，因此加上 `end=""`，避免每行之間多出空白行。

試著在 `sample.txt` 加上一行文字，再執行程式，看看輸出有什麼變化。

## 練習三：寫入檔案

```python
with output_file.open("w", encoding="utf-8") as file:
    file.write("這是寫入檔案的文字。\n")
```

- `"w"` 表示寫入模式。
- 檔案不存在時會建立檔案。
- 檔案已存在時，原本內容會被清除，再寫入新內容。
- `\n` 表示換行。

執行程式後，打開程式建立的 `practice_output.txt` 查看內容。想保留重要資料時，請小心使用 `"w"`。

## 練習四：附加內容

```python
with output_file.open("a", encoding="utf-8") as file:
    file.write("這段文字會加在檔案最後。\n")
```

`"a"` 是附加模式：檔案不存在時會建立檔案；檔案已存在時，會把新內容加在最後，不會清除原有內容。

## 動手挑戰

1. 在 `sample.txt` 加上自己的句子，再執行程式。
2. 連續執行兩次程式，觀察 `"w"` 和 `"a"` 對 `practice_output.txt` 的影響。
3. 把 `read()` 改成 `readline()`，觀察它一次會讀取多少內容。
4. 試著寫入兩行不同的文字，並用 `\n` 分隔。

## 常用檔案模式

| 模式 | 用途 | 注意事項 |
| --- | --- | --- |
| `"r"` | 讀取檔案 | 檔案必須已存在 |
| `"w"` | 寫入檔案 | 會清除檔案原有內容 |
| `"a"` | 在檔案末尾附加內容 | 不會清除原有內容 |
