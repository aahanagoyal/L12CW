import turtle
turtle.Screen().bgcolor("powderblue")
turtle.Screen().setup(500, 500)
turtle.Screen().title("Turtle")
poly=turtle.Turtle()
side=5
len=100
a=360/side
for i in range(side):
    poly.forward(len)
    poly.left(a)

turtle.done()