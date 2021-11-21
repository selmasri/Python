class Node:
    
    __slots__ = ['value', 'next']
    def __init__(self, value, next):
     
        self.value = value
        self.next = next
        #self.rank = gpa*100 + credits
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    
    #This function is to change the gpa for objects
    def set_value(self, my_value):
        self.value = my_value
    
    def __str__(self):
        return "A " + self.value + " node.\n"
    

    def __repr__(self):
        return "\n Node:\n  value = " + str(self.value) \
            + "\n  next node = " + str(self.next)
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.value == self.other
        else:
            return False     

def count(node):
    if node == None:
        return 0
    else:
        return 1 + count(node.get_next())      


def print_node(node_seq):
    if node_seq == None:
        print(None)
    else:
        print(node_seq.get_value(), ' ')
        print_node(node_seq.get_next())      



def main():

    sequence_of_one = Node('a', None)

    sequence_of_two =  Node('b', sequence_of_one)
    
    sequence_of_three = Node('c', sequence_of_two)
    
    sequence_of_four = Node('d', sequence_of_three)
    
    sequence_of_five = Node ('e', sequence_of_four)
    

    #print(count(sequence_of_four))
    #print(sequence_of_five)
    print_node(sequence_of_five)

main()