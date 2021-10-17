import array as arr
def binary_search(my_array, target, start = 0, end = 8):
    #end = len(my_array) -1 
    midpoint = (start + end) // 2
    #print(target)
    #print(my_array[midpoint])
    if target == my_array[midpoint]:
        #print("Found it from the first iteration")
        return midpoint
    elif target > my_array[midpoint]:
        start = midpoint + 1
        #print('Second half')
        binary_search(my_array, target, start, end)
    else:
        end = midpoint -1
        #print ('First half')
        binary_search(my_array, target, start, end)
    if start > end:
        return None
def main():
    an_array = arr.array('i', [5, 20, 30, 34, 45, 67, 78, 90, 97])
    my_target = int(input('Enter the target to search '))
    #print(an_array)
    print(binary_search(an_array, my_target))
main()
