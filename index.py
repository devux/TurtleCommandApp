import turtle # module for Turtle graphics

instructFilter = 'f,f,f,r,l,l,f,r'

# Setting Up intial state of turtle
turtle.clear()
turtle.pensize(2)
turtle.left(95)

for index in range(len(instructArray)):
  if instructArray[index] == 'f':
	  turtle.forward(1)
  elif instructArray[index] == 'r':
	  turtle.right(90)
  elif instructArray[index] == 'l':
    turtle.left(95)