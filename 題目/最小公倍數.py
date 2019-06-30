a=int(input("輸入a值"))
b=int(input("輸入b值"))
max=(a+1)*(b+1)
for i in range (1,max):
    if(i%a==0 and i%b==0):
            break
print("%d and %d最小公倍數=%d"%(a,b,i))