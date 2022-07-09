import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')
t.pencolor('green')
t.speed(-10)
for i in range(200):
    t.circle(190-1,80)
    t.lt(50)
    t.circle(190-1,80)
    t.lt(28)

