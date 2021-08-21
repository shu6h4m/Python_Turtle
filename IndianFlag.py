import turtle as s

s.penup()
s.goto(-400, 250)
s.pendown()
s.bgcolor("white")
s.color("#FF9933")
s.begin_fill()
s.forward(800)
s.right(90)
s.forward(167)
s.right(90)
s.forward(800)
s.end_fill()
s.penup()
s.left(90)
s.forward(167)
s.pendown()

s.color("green")
s.begin_fill()
s.forward(167)
s.left(90)
s.forward(800)
s.left(90)
s.forward(167)
s.end_fill()

s.penup()
s.goto(70, 0)
s.pendown()
s.color("navy")
s.begin_fill()
s.circle(70)
s.end_fill()

s.penup()
s.goto(60, 0)
s.pendown()
s.color("white")
s.begin_fill()
s.circle(60)
s.end_fill()

s.penup()
s.goto(-57, -8)
s.pendown()
s.color("navy")

for i in range(24):
    s.begin_fill()
    s.circle(3)
    s.end_fill()
    s.penup()
    s.forward(15)
    s.right(15)
    s.pendown()

s.penup()
s.goto(20, 0)
s.pendown()
s.begin_fill()
s.circle(20)
s.end_fill()

s.penup()
s.goto(0, 0)
s.pendown()
s.pensize(2)

for i in range(24):
    s.forward(60)
    s.backward(60)
    s.left(15)

s.done()


#coded by shu6h4m