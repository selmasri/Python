'''
This program prints a personalized "Hello!" message to the user.
author: Rubeus Hagrid
'''
def hello():
    """
    This function prompts the user to enter their name into 
    standard input and then prints a personalized message to
    standard output.
    """
    name = input("Enter your name: ")  # prompt the user
    # print the personalized message 
    print("Hello,", name, "!")
    #myname = "Samir"
    myage = 25.76
    name = name + " El-Masri"
    myage = myage + 12
    print(name, int(myage))



# don’t forget to call the function!
hello()
