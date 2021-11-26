#from stackclass import Stack


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    

def main():

    stack1 = Stack()

    print('Is the stack empty?', stack1.isEmpty())

    stack1.push(4)
    stack1.push('dog')
    stack1.push('This is an element of the stack')
    stack1.push(100.36)
    print('The top element of the stack is =', stack1.peek())
    stack1.push(True)

    print('the size of the stack is = ', stack1.size())

    print(stack1.isEmpty())

    stack1.push(8.4)
    print('The top element of the stack is =', stack1.peek())
    print('the size of the stack is = ', stack1.size())
    print(stack1.pop())

    print('the size of the stack is = ', stack1.size())
    print(stack1.pop())
    print('the size of the stack is = ', stack1.size())

main()