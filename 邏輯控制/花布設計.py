#設計理念：多邊形旋轉出花色，在使用六種不同的花色拼出花布。
#設計：北一女中10630819涂語優
#授權方式：	姓名標示─非商業性─相同方式分享



from turtle import *

#define funtion
def eight(s):
  for i in range(8):
    forward(s)
    left(360/8)
    
def six(s):
  for i in range(6):
   forward(s)
   left(60)
   
def five(s):
  for i in range(5):
   forward(s)
   left(360/5)
   
   

def flower1(s):
  for i in range(50):
    eight(s)
    left(36.4)

def flower2(s):
  #left()
  for i in range(42):
    six(s)
    left(60.42)
    
def flower3(s): 
  for i in range(42):
    six(s)
    left(61)
    
def flower4(s):
    for i in range(40):
      five(s)
      left(72.5)
      
    
def flower5(s):
    for i in range(35):
      five(s)
      left(72.7)
      
      
def flower6(s):
  for i in range(48):
    eight(s)
    left(60.6)
      
speed(0)

#initialize
start_x = -200
start_y =  200


size = 40
gap = 25
n = 10 

#start drawing
for j in range(n):
  for i in range(n):
    penup()
    x = start_x + (2*size+gap)*i
    y = start_y - (2*size+gap)*j
    goto(x,y)
    pendown()

    if i==j or i+6==j or j+6==i:
      flower3(27)
    elif i+1==j or j+1==i or i+7==j or j+7==i:
      flower4(32)
    elif i+2==j or j+2==i or i+8==j or j+8==i:
      flower6(20)
    elif i+3==j or j+3==i or i+9==j or j+9==i:
      flower2(27)
    elif i+4==j or j+4==i:
      flower5(32)
    elif i+5==j or j+5==i:
      flower1(20)
      
      
      
hideturtle()  
done()