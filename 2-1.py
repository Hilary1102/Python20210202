import random #匯入random模組
n=random.randint(1,20)

while True: #一直
    ans = int(input("請輸入數字")) #回答變成數字型態
    if n == ans:
        print("答對")
        break #程式結束
    else:
        print("答錯")
        