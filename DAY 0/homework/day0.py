from turtle import *

#we want to point a house
speed(30)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)
 
forward(200)
left(90)

#end of square

#drawing a door

forward(200)
left(90)

forward(120)


penup()
goto(200, 200)
pendown()

color("green")
begin_fill()

left(120)
forward(200)


left(120)
forward(200)
end_fill()

penup()

goto(70,0)
pendown()
color("yellow")
begin_fill()

right(150)

forward(120)
right(90)

forward(60)
right(90)

forward(120)

end_fill()


#the door is finnished
penup()

goto(10,120)

pendown() 

color("blue")
begin_fill()

right(180)
forward(30)

right(180)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

end_fill()

penup()
goto(190,110)

pendown()

color("blue")
begin_fill()

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)

end_fill()

exitonclick()