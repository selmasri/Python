import turtle as t


def draw_rectangle(length, width):
   t.begin_fill()
   t.fillcolor('blue')
   for i in range(2):
       t.forward(width)
       t.left(90)
       t.forward(length)
       t.left(90)
   t.end_fill()
   t.setposition((length+width)/2, 0)
   return length*width
   
def main():
   lengthh = 200
   width= 400
   print('The perimeter is: ', draw_rectangle(lengthh, width))
   input('OK')

main()