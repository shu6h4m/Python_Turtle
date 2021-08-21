import turtle as t

t.bgcolor('black')
#colors =('cyan','pink','cyan','pink')
colors =('white','white','white','white')
t.speed(0)
for i in range(150):
    t.pencolor(colors[i%4])
    t.width(2)
    t.forward(i)
    t.circle(90,steps=2)
    t.forward(i)
    t.right(45)
t.hideturtle()
t.done()