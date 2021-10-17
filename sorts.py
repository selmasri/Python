import array as ar


def swap(a_array, a, b):
    temp = a_array[a]
    a_array[a] = a_array[b]
    a_array[b] = temp

def shift(b_array, n):
    while n > 0:
        if b_array[n] < b_array[n-1]:
            swap(b_array, n, n-1)
        n = n-1

def insertion_sort(c_array):
    for index in range(len(c_array)):
        shift(c_array, index)

def my_test():
    return 'Samir'

def main():
    #my_array = ar.array('i', [100, 78, 50, 125, 65, 200, 56, 78, 210, 82])
    #print(my_array)
    #swap(my_array, 5, 0)
    #swap(my_array, 5, 6)
    #insertion_sort(my_array)
    #print(my_array)
    result = my_test()
    print(result)
    print(type(result))

main()
