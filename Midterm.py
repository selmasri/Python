import turtle


def draw_rectangle(length, width):
   turtle.fillcolor("blue")
   turtle.begin_fill()
   turtle.up()
   turtle.left(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(100)
   turtle.left(180)
   turtle.down()
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(width)
   turtle.left(90)
   turtle.forward(length)
   turtle.left(90)
   turtle.forward(width)
   turtle.end_fill()
   turtle.up()
   turtle.home()



def main():
   #addition(1, 2, 3)
   #change_array[an_array]
   draw_rectangle(200, 100)
   input('o')
main()