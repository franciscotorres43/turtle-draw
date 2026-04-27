import turtle
import math

total_distance = 0
prev_point = None

screen = turtle.Screen()
screen.setup(width=450, height=450)

TEXTFILENAME = 'turtle-draw.txt'

TEXTFILENAME = input('Enter the name of the text file: ')

print ('TurtleDraw')

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()

print ('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print (line, end = '')
    parts = line.split()

    if len(parts) == 3:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.color(color)

        if prev_point is not None and turtleDraw.isdown():
            px, py = prev_point
            segment = math.dist((px, py), (x, y))
            total_distance += segment

        turtleDraw.goto(x, y)
        turtleDraw.pendown()

        
        prev_point = (x, y)

    elif len(parts) == 1:
        turtleDraw.penup()
        prev_point = None  

    line = turtleDrawTextfile.readline()

turtleDraw.penup()
turtleDraw.goto(0, -200)
turtleDraw.color("black")
turtleDraw.write(f"Total connected distance: {total_distance:.2f}", align="center", font=("Arial", 14, "normal"))

input("Press Enter to close...")
turtleDrawTextfile.close()



print('\nend')
