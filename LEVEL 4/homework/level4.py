from turtle import*
speed(99999999999999999)

#სასახლის აშენება
penup()
goto(-250,-280)
pendown()
color('grey')
begin_fill()
left(90)
forward(300)
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(300)
end_fill()
right(90)
forward(50)
color('black')
begin_fill()
left(45)
forward(150)
right(90)
forward(150)
end_fill()

#ვხატავთ კოშკს

penup()
goto(51,-280)
pendown()
color('black')
begin_fill()

left(45)
left(90)
forward(500)
right(90)
forward(150)
right(90)
forward(500)
right(90)
forward(150)
end_fill()

# ვხატავთ კოშკის სახურავს

penup()
goto(50,220)
pendown()
color('grey')
begin_fill()
right(180)
left(45)
forward(110)
right(90)
forward(110)


end_fill()

#ვხატავთ მეორე კოშკს

penup()

goto(-250,-280)
pendown()
color('black')
begin_fill()
left(135)
forward(500)
left(90)
forward(150)
left(90)
forward(500)
left(90)
forward(500)
end_fill()

#ვხატავთ მეორე კოშკის სახურავს

penup()
goto(-250,220)
pendown()
color('grey')
begin_fill()
left(131)
forward(115)
left(100)
forward(110)
end_fill()

#ვხატავთ დროშას

penup()
color('black')
goto(-105,115)
pendown()
right(180)
forward(20)
left(39)
forward(150)
right(90)
forward(120)
right(90)
forward(80)
right(90)
forward(120)
# ვწერთ გოას დროშაში
penup()
goto(-80,260)
pendown()
right(180)
forward(25)
right(180)
forward(25)
left(90)
forward(45)
left(90)
forward(25)
left(90)
forward(15)
left(90)
forward(7)
left(90)
forward(3)

penup()

goto(-45,230)

pendown()

circle(15)

penup()
goto(-8,215)
left(170)
pendown()
forward(50)
right(145)
forward(60)
right(180)
forward(25)
left(65)
forward(25)















exitonclick()