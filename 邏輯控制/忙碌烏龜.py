# there is a little bug, fix it
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

for i in range(1, 12):
   tina.right(30)
   for j in range(1, 4):
      tina.forward(100)
      tina.right(90)  