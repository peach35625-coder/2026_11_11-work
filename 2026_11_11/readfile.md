# Python 檔案操作：一步一步練習

歡迎開始練習！本指南會帶你使用 Python 讀取文字檔、逐行讀取、寫入新內容，以及在檔案最後附加文字。

## 你會用到的檔案

請將以下檔案放在同一個資料夾（本專案已提供）：

- `readfile.md`：本指南。
- `readfile.py`：可以直接執行的完整練習程式。
- `sample.txt`：提供給程式讀取的範例檔案。
- `student.csv`：提供給你練習讀取表格資料的範例檔案。

`sample.txt` 的範例內容如下：

```text
你好！這是提供給你的範例文字檔。
第一行：Python 可以讀取文字檔。
第二行：每一行都可以分開處理。
試著修改這個檔案，再執行 readfile.py。
```

## 第一步：執行練習程式

在終端機切換到這些檔案所在的資料夾，輸入：

```powershell
python readfile.py
```

程式會依序顯示讀取整份檔案、逐行讀取、寫入及附加內容的結果，並在同一個資料夾建立 `practice_output.txt`。

## 第二步：認識檔案路徑

在 `readfile.py` 中，這兩行找到程式旁邊的範例檔和輸出檔：

```python
from pathlib import Path

sample_file = Path(__file__).with_name("sample.txt")
output_file = Path(__file__).with_name("practice_output.txt")
```

- `Path` 是 Python 用來表示檔案路徑的工具。
- `__file__` 代表目前這支 Python 程式的位置。
- `with_name(...)` 會在相同資料夾中指定另一個檔案名稱。

因此，不論從哪個資料夾執行程式，它都會尋找 `readfile.py` 旁邊的 `sample.txt`。

## 第三步：讀取整份檔案

```python
with sample_file.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

1. `"r"` 是讀取模式（read）。
2. `read()` 會取出檔案中的全部文字。
3. `encoding="utf-8"` 讓中文可以正確讀取。
4. `with` 區塊結束後，Python 會自動關閉檔案。

打開 `sample.txt` 看看內容，再和螢幕上的輸出比較。

## 第四步：一次讀取一行

```python
with sample_file.open("r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

`for line in file` 會一行一行讀取。每行通常已經包含換行符號，所以 `print` 加上 `end=""`，避免行與行之間多出空白。

**動手試試：**在 `sample.txt` 最後加上一行自己的文字，再執行程式，看看輸出是否也多出那一行。

## 第五步：寫入檔案

```python
with output_file.open("w", encoding="utf-8") as file:
    file.write("這是寫入的第一行。\n")
    file.write("這是寫入的第二行。\n")
```

- `"w"` 是寫入模式（write）。
- 如果檔案不存在，Python 會建立它。
- **如果檔案已存在，原內容會被清除。**
- `\n` 代表換行。

執行程式後，打開 `practice_output.txt` 查看寫入的內容。練習前請勿把 `"w"` 用在存有重要資料的檔案上。

## 第六步：在檔案最後附加內容

```python
with output_file.open("a", encoding="utf-8") as file:
    file.write("這一行會加在檔案最後。\n")
```

`"a"` 是附加模式（append）。檔案不存在時會建立檔案；檔案已存在時，新文字會加在最後，不會清除原有內容。

## 第七步：自己動手挑戰

1. 在 `sample.txt` 寫入自己的句子，執行程式查看結果。
2. 在 `readfile.py` 找到 `"w"`，理解它如何寫入 `practice_output.txt`。
3. 將 `"w"` 改成 `"a"` 後再執行，觀察舊內容是否保留。想恢復原本練習流程時，記得改回 `"w"`。
4. 將 `file.read()` 改成 `file.readline()`，看看一次會讀到什麼內容。
5. 在 `file.write(...)` 中使用 `\n`，試著寫入多行文字。

## 第八步：讀取 CSV 學生資料

`student.csv` 是逗號分隔值（CSV）檔案，可以用試算表開啟，也可以用 Python 的 `csv` 模組讀取。請在 `readfile.py` 中加入以下程式，或另存為一支新的 Python 練習程式：

```python
import csv
from pathlib import Path

student_file = Path(__file__).with_name("student.csv")

with student_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(
            f"{student['name']}："
            f"{student['age']} 歲，"
            f"成績 {student['score']} 分"
        )
```

第一列是欄位名稱，因此 `DictReader` 可以用 `student["name"]`、`student["age"]` 等欄位名稱取得資料。

**動手試試：**

1. 在 `student.csv` 新增一位學生，重新執行程式。
2. 只印出成績：`print(student["score"])`。
3. 試著把 `student["score"]` 轉成整數：`int(student["score"])`，再判斷是否及格。

## 常用檔案模式整理

| 模式 | 用途 | 注意事項 |
| --- | --- | --- |
| `"r"` | 讀取檔案 | 檔案必須已存在。 |
| `"w"` | 寫入檔案 | 檔案不存在會建立；已存在則清除原內容。 |
| `"a"` | 在檔案最後附加內容 | 不會清除原有內容。 |
