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

def function(n):
    if n < 10:
        function(n+1)
        print(n)
    return 0


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

def func_caller(a_func, x):
    print(a_func.__name__)
    result = a_func(x)
    print(result)

def square_it(y):
    return y * y

def double_it(z):
    return z * 2

def evens(n):
    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum

def odds(n):
    sum = 0
    for i in range(n+1):
        if i % 2 != 0:
            sum += i
    return sum

def runner(a_func, n):
    print(a_func.__name__)
    result = a_func(n)
    print(result)

def cat(array1, array2):
    result = [0 for a in range(len(array1)+len(array2))]
    #result = arr.array('i', [0,0,0,0,0,0,0,0])
    for index in range(len(array1)):
        result[index] = array1[index]
    
    for index in range(len(array2)):
        result[index + len(array1)] = array2[index]
    return result
    #my_array = [0 for a in range(3)]
def tuples():
    tupa = (1, 2, 3, 4)
    tupb = ('a', 1, False, 3.14)
    tupc = tuple("abcd")
    tupb[0] = 'b'
    print(tupb[0])

def changing(a_list):
    length = len(a_list) 
    for index in range(length):
        a_list[index] = ra.randint(0, length)
    return a_list

def appending(a_string):
    a_list = []
    for index in range(len(a_string)):
        a_list.append(a_string[index])
    return a_list

def pop():
    a_list = ["a", "b", "c", "d", "e"]
    print(a_list)
    aa = a_list.pop(0) # ["b", "c", "d", "e"]
    print(a_list)
    ee = a_list.pop()  # ["b", "c", "d"]
    print(a_list)
    print(aa)
    print(ee)

def insert():
   b_list = [2, 3]
   print(b_list)
   b_list.insert(0, 1) # [1, 2, 3]
   print(b_list)
   b_list.insert(6, 4) # [1, 2, 4, 3]
   print(b_list)   

def tuples():
    tupa = (1, 2, 3, 4)
    tupb = ('a', 1, False, 3.14)
    tupc = tuple("abcd")
    print(tupa)
    print(tupb)
    print(tupc)

def tuple_equality(a_tuple, a_list):
    if a_tuple == a_list:
        print('Tuples are equal with ==')
    
    if a_tuple is a_list:
        print('Tuples are equal with is')

def slicing():
    a_string = "Buttercup FTW"
    doggo = list(a_string)
    
    print(type(doggo))
    
    print(doggo)
    
    slice1 = doggo[2:6]
    slice2 = doggo[8:11]
    print('slice1 = ', slice1)
    print('slice2 = ', slice2)
    print(type(slice1))
    
    print(doggo[:6])
    print(doggo[3:])
    print(doggo[:])
    print(doggo[2:10:2])
    print(doggo[-3:])
    print(doggo[:-4])
    
    print(doggo[::-2])
    print(doggo[::-1])
    

def b_sorting():
    #a_list = [2, 1, 5, 4, 3]
    a_list = ['b','a', 'A', 'c', 'C']
    b_list = sorted(a_list)
    #b_list = sorted(a_list, reverse=True)
    #b_list = sorted(a_list, reverse=False)
    print(b_list)
    print(a_list)
    
    #a_list.sort()
    #a_list.sort(reverse = True)
    #b_list.sort(key=evens_before_odds)
    a_list.sort(key=str.lower)
    print(a_list)
    a_list.sort(key=str.lower, reverse=True)
    print(a_list)

def concat():
    a_list = ["a"]
    b_list = ["b"]
    b_list = a_list + b_list
    print(b_list)
    b_list = b_list + [1, 2, 3]
    print(b_list)
    first = ["Butt"]
    first += ["ercup"]
    print(first)
    print(first.pop(0), end="")
    #print(first)
    print(first.pop())
    print(first)

    lst = []
    lst.insert(0, 123)
    lst.insert(1, 'RIT')
    #print(lst.insert(1, 'RIT'))
    print(lst)

def packer():
    a = 50
    b = 'RIT'
    c = True
    d = 3.78
    return a, b, c, d

def swapper(a_list):
    half = int(len(a_list)/2)
    print(half)
    b_list = []
    for index in range(half):
        b_list.insert(index, a_list.pop(0))
    
    return a_list + b_list

def my_table(x, a_value = 0):
    #for index in range(y):
    my_list = [a_value for _ in range(x)]
    print(my_list)
    print(my_list[2][2])
    print(my_list[2])
    my_list[0] = [20, 7, 41, 25, 16]
    my_list[2] = [10, 17, 2, 5, 160, 200, 56, 78, 92]
    print(my_list)
    print(my_list[2][4])
    my_list[2][0] = 100
    print(my_list)
    print(type(my_list))
    
    for i in range(x):
        print(my_list[i])

def sets():
    my_set = {1, 4}
    print(type(my_set))
    a_set = {1, 2, 3, 20, 18, 7, 15}
    d_set = {1, 2, 7, 20, 300, 400}
    b_set = {18, 7, 15, 1, 2, 3, 20}
    c_set = {3, 2, 15}
    for number in a_set:
        print(number, end = " ")
    
    print()

    #a_list = sorted(a_set)
    a_list = list(a_set)
    print(a_list)

    #b_set.add(100)

    if a_set is b_set:
       print("OK")

    #print(a_set)
    print(b_set)
    a_set.add(4)
    print(a_set)

    if 13 in a_set:
       print("13 is in the set!")
    else:
       a_set.add(13)

    a_set.add(2)

    for value in a_set:
      print(value)
    b = 200
    a_set.add(b)
    print(a_set)
    a_new_list = sorted(a_set)
    print(a_new_list)
    print(type(a_new_list))
    a_new_set = set(a_new_list)

    if a_set == a_new_set:
        print("They are the same sets")


    b_set = set("abcdcba")
    
    print(b_set) # {'c', 'd', 'b', 'a'}
    
    for char in b_set:
        print(char, end = ' ')

    a_list = [2, 5, 3]
    a_tuple = (6, 'RIT', True)
    c_set = set(a_tuple)
    
    #print(type(c_set))
    #print(type(a_list))
    #print(c_set)

def main():
   sets()
   #my_value = [2, 3, 4, 5, 6]
   #my_value = 5
   #my_table(4, my_value)
   #my_list = []
   #my_list = [10]
   #my_list = [23, 15, 20]
   
   #print(my_list)
   #print(swapper(my_list))
   #my_list = [6,8,5,9,7,3,10,56,20,33]
   #my_list = [x**2 for x in range(10)]
   #my_list = [n for n in range(1, 10, 2)]
   #my_list = [char + ' RIT' for char in "EXPO Dubai"]
   #my_list = ['rit' for _ in range(10)]
   #my_list = [23 for _ in range(10)]
   #data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
   #my_list = [x//2 for x in data]
   #my_list = [q for q in data if q % 2 != 0]
   #my_list = [q for q in data if q >= 4 and q < 8]
   #print(my_list)

   
    #packed = packer()
    #print(type(packed))
    #print(packed)
    
    #for index in range(len(packed)):
    #    print(packed[index])
    

'''
    #b_sorting()
    #concat()
    #b_sorting()
    #slicing()
    #a_list = [1, 'Samir', True]
    #a_tuple = tuple(a_list)
    #print(a_tuple)
    #tuple_equality(a_tuple, a_list)
    #tuples()
    #pop()
    #insert()

    
    tuples()
    my_list = (2,3,5,18, 'Masri')
    my_string = 'Samir'
    #print(changing(my_list))
    print(appending(my_string))

    #an_array1 = arr.array('i', [56, 89, 78, 99, 1000])
    #print(type(an_array1))
    #an_array2 = arr.array('i', [1089, 78, 9898, 78, 20, 50])
    
    #result_array = cat(an_array1, an_array2)
    #print(result_array)
    
    
    my_array2 = []
    print(type(my_array2))
    
    my_array2.append(3)
    my_array2.append(4)
    print(my_array2)
    print(my_array2[1])
    print(type(my_arrays))
    print(len(my_array2))

    my_array = [0 for a in range(3)]
    print(my_array)
    print(type(my_array))
    #print_odds(an_array)
    #print_odds_rec(an_array)
    #countdown(994) # recusrion depth is 993 max
    #print(factorial(997))
    #l = factorial(3)
    #my_time()
    #my_arrays()
    #my_random()
    #array_search(number)
    #my_number = int(input("enter number = "))
    #count_up(my_number)
    #func_caller(square_it, 100)
    #func_caller(double_it, 1000)
    #print(evens(10))
    #print(odds(10))
    #runner(evens, 100)
    #runner(odds, 10)
    #print(evens(10))
    '''
    #array = arr.array('i',[1,4])
    
main()
