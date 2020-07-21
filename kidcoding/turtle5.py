import turtle

s = turtle.Screen()
t = turtle.Turtle()

for step in range(100):
    t.circle(step)
    t.left(91)
s.exitonclick()