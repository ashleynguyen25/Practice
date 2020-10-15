import turtle as trtl

trtl.speed(0)


#Makes a 18 circles to create a larger circle
def flower_petals():
  for i in range(18):
    trtl.penup()
    trtl.forward(10)
    trtl.right(20)
    trtl.pendown()
    trtl.circle(20)

#Stem of the flower
def stem_of_flower():
  trtl.penup()
  trtl.goto(10,-92)
  trtl.right(90)
  trtl.pendown()
  trtl.forward(100)

flower_petals()
stem_of_flower()