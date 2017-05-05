import turtle #module for Turtle graphics
import re #module for Regular expression operations


# Get Instruction from user
print "Enter a Instruction with the following words: F,R,L \n",
instruct = raw_input()

#Removing unwanted string expect -flrFL and R
instructFilter = re.sub(r'[^flrFLR]', '', instruct)

print "Accepted string from your Input \n"
print instructFilter
instructArray = list(instructFilter)

# Setting Up intial state of turtle
turtle.clear()
turtle.pensize(2)
turtle.left(95)

totalLength = len(instructArray)
for index in range(len(instructArray)):
  if instructArray[index] == 'f':
	  turtle.forward(1)
  elif instructArray[index] == 'r':
	  turtle.right(90)
  elif instructArray[index] == 'l':
    turtle.left(95)

  # Last cycle of for loop
  if index == totalLength -1:
		print turtle.pos()