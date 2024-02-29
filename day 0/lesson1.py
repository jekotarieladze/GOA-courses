from turtle import*

#we want to paint a house

#step 1: draw a source

width(7)
color("orange")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#making the brown windows
color("blue")
begin_fill()
left(120)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()

#make a second windows cuz why not?
penup()
goto(137,200)
pendown()
color("blue")
begin_fill()
right(90)
forward(65)
right(90)
forward(65)
right(90)
forward(65)
right(90)
forward(65)
end_fill()

end_fill()


exitonclick()