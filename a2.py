import turtle
wind=turtle.Screen()
wind.bgcolor("powderblue")
p=turtle.Turtle()
s=0
while True:
 for i in range(4)   :
       p.fd(s+1) 
       p.left(90)
       s=s-5
 s=s+1       
