def function():
    import random
    number = random.randrange(1, 100)
    for i in range(5):
        print("請猜一個數字")
        x=eval(input())
        i+=1
        if(x==number):
            print("Congratulations! You win!")
            break
        elif(x>number):
            print("太大了")
        else:
            print("太小了")
    print("要再來一次嗎?")

function()
z=eval(input("yes打0,no打1\n"))

while z==0:
    function()
   
    z=eval(input("yes打0,no打1\n"))
else:
    print("結束了")