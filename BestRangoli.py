import turtle as s

s.bgcolor('black')
colors =('cyan','pink','cyan','pink')
#colors =('white','white','white','white')
s.speed(0)
for i in range(60):
    s.pencolor(colors[i%4])
    s.width(2)
    s.forward(i)
    s.circle(90,steps=4)
    s.forward(i)
    s.right(45)
s.hideturtle()
s.done()
#Coded by shu6h4m