class Queue:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def enqueue(self, item):
         self.items.append(item)

     def dequeue(self):
         return self.items.pop(0)

     
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    

def main():

    queue1 = Queue()

    print('Is the queue empty?', queue1.isEmpty())

    queue1.enqueue(4)
    queue1.enqueue('dog')
    queue1.enqueue('This is an element of the queue')
    queue1.enqueue(100.36)
    print('The top element of the queue is =', queue1.peek())
    queue1.enqueue(True)

    print('the size of the queue is = ', queue1.size())

    print(queue1.isEmpty())

    queue1.enqueue(8.4)
    print('The top element of the queue is =', queue1.peek())
    print('the size of the queue is = ', queue1.size())
    print(queue1.dequeue())

    print('the size of the queue is = ', queue1.size())
    print(queue1.dequeue())
    print('the size of the queue is = ', queue1.size())

main()