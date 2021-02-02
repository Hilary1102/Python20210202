import random 
n=random.randint(1,20)
t=0
while True: 
    ans = int(input("請輸入數字")) 
    if   n == ans:
        t=t+1
        print("答對了")
        print("玩了"+str(t)+"次")
        break 
    elif ans < n:
        t=t+1
        print("太小") 
    elif ans > n:
        t=t+1
        print("太大")
    elif t>5:
        break
