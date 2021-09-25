import math

#triangle_base = 0

def test_triangle_height_valid():
    result = triangle_height(-1) 
    assert result == None, "Condition 1 Failed"
    #print("result is None because because base is negative")
    print("Triangle_height =", result)

"""
def triangle_height(base_length):
    print(base_length)


def triangle_height(base_length):
    if base_length < 0:
        return None
"""
def triangle_height(base_length):
    height = math.sqrt(base_length**2 - (base_length/2)**2)
    print(height)
    if base_length <0:
        print("You entered a negative number for triangle base")
        return None
    return height


def main():
    #triangle_base = input("Enter the Triangle base ")
    test_triangle_height_valid()


main()