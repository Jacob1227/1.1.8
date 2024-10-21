import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
d=0
x=5
y=7
# TODO: move turtles across and down screen, stopping for collisions
for step in range(10):
  d=d+1
  for ht in horiz_turtles:
    for vt in vert_turtles:
      ht.forward(x+1)
      vt.forward(y+1)
      if (x>10):
        x=3
      if (y>10):
        y=5
      if (abs(ht.xcor() - vt.xcor()) < 20):
         if (abs(ht.ycor() - vt.ycor()) < 20):
          vt.backward(40)
          vt.color("red")
          ht.backward(40)
          ht.color("red")
for ht in horiz_turtles:     
    ht.color("blue")
for vt in vert_turtles:
    ht.color("blue")
         
  
    


wn = trtl.Screen()
wn.mainloop()
