from turtle import *
bgcolor('black')
hideturtle()
speed(100)
for i in range(120):
  if i %2==0:
    color('cyan')
  else:
    color('magenta')
  forward(i*4)
  left(91)
done()