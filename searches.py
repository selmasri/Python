import array as arr

def binary_search(my_array, target, start = 0, end = None):
    end = len(my_array) -1
    midpoint = (start + end) // 2
    print(target)
    print(my_array[midpoint])
   
    if target == my_array[midpoint]:
        return midpoint
    
    elif target > my_array[midpoint]:
        start = midpoint + 1
        print('Second half')
        binary_search(my_array, target, start)
    else:
        end = midpoint -1
        
        print ('First half')
        binary_search(my_array, target, end)
    if start > end:
        return None
   


def main():
    an_array = arr.array('i', [100, 235, 70, 8, 5, 453, 56, 89, 78, 99, 20, 676, 87,9898])
    my_target = int(input('Enter the target to search '))
    print(an_array)
    print(binary_search(an_array, my_target))



main()
