class Stack:
    
    __slots__ = ['size', 'is_empty']
    def __init__(self, size, is_empty):
     
        self.size = size
        self.is_empty = is_empty
        #self.rank = gpa*100 + credits
    
    def __repr__(self):
        return "\n Stack:\n  size = " + str(self.size) \
            + "\n  is_empty = " + str(self.is_empty)

    def get_size(self):
        return self.size

    def get_is_empty(self):
        return self.is_empty
    def push(self, value):
        



def main():

    stack1 = Stack(5, False)
    print(stack1)
    #stack1.push('a')
    stack2 = Stack()


main()
