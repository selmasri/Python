import turtle

angle1 = 10
angle2 = 30
angle3 = 40
b = 20

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up()
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)


def turtle_state():
    turtle.isdown()
    turtle.heading()
    turtle.xcor()
    turtle.ycor()


def square(my_pencolor, my_fillcolor, angle):
    turtle.begin_fill() 
    turtle.color(my_pencolor)
    turtle.bgcolor("blue")
    turtle.fillcolor(my_fillcolor)
    
    turtle.pensize(12)
    turtle.left(angle)
    #turtle.down()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

"""
def square(a):
    #turtle.down()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
"""

def main():
    #test_drive()
    #input("Press enter to continue...")
    #turtle_state()
    square("red", "Teal", angle1)
    square("DarkOrchid", "Fuchsia", angle2)
    square("DarkRed", "Chartreuse", angle3)
    input("Press enter to continue...")
    """
    b = input("Enter the length of the square ")
    my_square_length = int(b)
    square(my_square_length)
    
    input("Press enter to continue...")
    b = input("Enter the length of the square ")
    b = int(b)
    square(b)
    input("Press enter to continue...")
    #turtle_state()
    """
main()
