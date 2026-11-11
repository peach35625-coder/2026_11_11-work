from pathlib import Path


# 範例檔與輸出檔都放在這支 Python 程式旁邊。
sample_file = Path(__file__).with_name("sample.txt")
output_file = Path(__file__).with_name("practice_output.txt")


def main():
    print("練習 1：讀取整個檔案")
    # with 會在讀取完成後自動關閉檔案；encoding="utf-8" 可正確處理中文。
    with sample_file.open("r", encoding="utf-8") as file:
        content = file.read()
    print(content)

    print("練習 2：一次讀取一行")
    with sample_file.open("r", encoding="utf-8") as file:
        for line in file:
            # 每行通常已經有換行符號，print 再加換行會多出空白行。
            print(line, end="")

    print("\n練習 3：建立並寫入新檔案")
    # "w" 是寫入模式；檔案不存在時會建立，已存在時會清空再寫入。
    with output_file.open("w", encoding="utf-8") as file:
        file.write("這是 Python 寫入的第一行。\n")
        file.write("試著看看檔案內容吧！\n")
    print(f"已寫入：{output_file.name}")

    print("\n練習 4：在檔案結尾附加內容")
    # "a" 是附加模式，不會清除原有內容。
    with output_file.open("a", encoding="utf-8") as file:
        file.write("這一行是後來附加的。\n")

    print("目前輸出檔的內容：")
    with output_file.open("r", encoding="utf-8") as file:
        print(file.read(), end="")

    print("\n\n自己動手試試：")
    print("1. 在 sample.txt 多加一行，再重新執行程式。")
    print("2. 將寫入模式改成 'w'，觀察舊內容是否保留。")
    print("3. 將寫入模式改成 'a'，觀察新內容會出現在哪裡。")


if __name__ == "__main__":
    main()
