import array as arr
import random as ra
import time

number = 0
#sum = 0

def print_odds(my_array):
    for index in range(len(my_array)):
        if my_array[index] % 2 != 0:
            print(my_array[index], ' ', end = '')



def print_odds_rec(my_array, index = 0):
    if my_array[index] % 2 != 0:
            print(my_array[index], ' ', end='')
    index += 1
    if index == len(my_array):
        return 1
    print_odds_rec(my_array, index)


def countdown(my_number, sum = 0):
    if my_number >= 0:
        print(my_number)
        sum += my_number
    else:
        print('Sum = ', sum)
        return 0
    countdown(my_number-1, sum)

def factorial(n):
    if n < 0:
       return None
    elif n == 0 or n == 1:
       return 1
    else:
       fact_rest = factorial(n - 1)
       return n * fact_rest
    
def my_time():
    
    begin = time.perf_counter()
    sum = 0
    
    #for number in range(100000000):
    #    sum += number
    number = input("Enter number to search ")
    array_search(number)

    end = time.perf_counter()
    elapsed = end - begin
    
    print("elapsed time:", elapsed)


def array_search(my_number):
    array_a = arr.array('i', [100, 234, 70, 8, 5, 100, 454, 56, 89, 78, 98, 1000, 20, 676, 87,9898])
    for i in range(len(array_a)):
        if array_a[i] == int(my_number):
            print("The serach is successful with index =", i)
            return i

def my_random():
    
    ra.seed(1)
    number = ra.randint(1, 6)
    print(number)
    for _ in range(10):
        number = ra.randint(1, 6)
        #number = ra.randrange(2, 20, 2)
        #number = ra.random()
        print(number, end=" ")

     #print()




def my_arrays():
    """
    my_arr = arr.array('u', 'hello 2641')

    print(len(my_arr))

    my_arr[9] = 'S'

    print(my_arr)
    print(my_arr[9])
    
    my_arr('u', 'hello \u2641')
    my_arr('l', [1, 2, 3, 4, 5])
    my_arr('d', [1.0, 2.0, 3.14])
"""


    #array_a = arr.array('u', ['S', 'a','m', 'i', 'r'])
    array_a = arr.array('i', [100, 234, 70, 8, 5, 100, 454, 56, 89, 78, 98])
   
    print(len(array_a))
    print(array_a)
    print(array_a[3])
    array_a[3] = 1000
    print(array_a[3])
    
    length = len(array_a)

    for i in range(length):
        print(array_a[i])

    for index in range(length):
        array_a[index] = index * 5
        print(array_a[index])
    print(array_a)

def count_up(number, count = 0): 
    if count <= number:
        print(count)
        count_up(number, count+1)
    else:
        return 0


def main():
    #an_array = arr.array('i', [100, 235, 70, 8, 5, 100, 453, 56, 89, 78, 99, 1000, 20, 676, 87,9898])
    #print_odds(an_array)
    #print_odds_rec(an_array)
    #countdown(994) # recusrion depth is 993 max
    #print(factorial(997))
    #l = factorial(3)
    #my_time()
    #my_arrays()
    #my_random()
    #array_search(number)
    my_number = int(input("enter number = "))
    count_up(my_number)
main()
