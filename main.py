import turtle as trtl

trtl.speed(0)

#Makes a 18 circles to create a larger circle
for i in range(18):
  trtl.penup()
  trtl.forward(10)
  trtl.right(20)
  trtl.pendown()
  trtl.circle(20)