import turtle
#x = 5
samir = 45
angle1 = 10
angle2 = 30
angle3 = 40
b = 20

def test_drive():
    turtle.forward(100)
    #turtle.setheading(90)
    #turtle.setheading(30)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(100)
    #turtle.setheading(127)

    turtle.goto(50,100)
    turtle.up()
    turtle.home()
    turtle.left(45)
    #turtle.down()
    #turtle.circle(25)

def addition(a, b):
    x = a + b
    print(x)
    
def parameters(ax, bx, cx, dx):
    x = ax + bx
    print(x)
    print(cx, dx)
    print("Samir = ", samir)





def turtle_state():
    pen_state = turtle.isdown()
    turtle_angle = turtle.heading()
    x = turtle.xcor()
    y = turtle.ycor()
    print(int(x), int(y), pen_state, turtle_angle)


def square(my_pencolor, my_fillcolor, angle):
    turtle.begin_fill() 
    turtle.color(my_pencolor)
    turtle.bgcolor("gold")
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
    #square(100)
    #print(x)
    #test_drive()
    #input("Press enter to continue...")
    #turtle_state()
    #x = input("Enter the first number ")
    #y = input("Enter the second number ")
    #addition(int(x),int(y))
    #parameters(4, 3, 2, 1)
    #parameters("a", "b", "c", "d")
    #print("Samir = ", samir)
    
    #parameters(35, 56)
    #parameters("Samir", " El-Masri")
    #input("Press enter to continue...")
    #turtle_state()
    
    
    turtle.tracer(False) # toggle off
    square("red", "Teal", angle1)
    square("DarkOrchid", "Fuchsia", angle2)
    square("DarkRed", "Chartreuse", angle3)
    turtle.pensize(5)
    turtle.speed(0)
    turtle.circle(100)
    turtle.tracer(True)
    input("Press enter to continue...")
   
    #input("Press enter to continue...")
    """
    turtle.tracer(False) # toggle off
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    '''The image will not appear until
        you toggle the tracer back on.'''
     
    input("Press enter to continue...")
    turtle.tracer(True)
    input("Press enter to continue...")
  
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