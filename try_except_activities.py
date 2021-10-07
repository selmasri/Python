def my_addition():  
    
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))

        print("x + y =", (x + y))
    
    except:
        print("Invalid integer(s).")
        print("Try again.")
    
    print("Program complete.")



def simple_division(num, denom):
    #try:
    print("x / y =", (num/denom))
    #except:
    print("Divide by 0 or wrong data type")
    print("Try again.")

    print("Program complete.")


def test_for_exception():
    # setup
    numerator = 10
    denominator = 0
    # invoke
    try:
        simple_division(numerator, denominator)
        assert (False)
    # analyze
    except ArithmeticError:
        assert (True)


def my_division():
    attempts = 4
    while True:
        x_input = input("Enter x: ")
        y_input = input("Enter y: ")

        try:
            x = int(x_input)
            y = int(y_input)

            print("x / y =", (x/y))

        except ValueError as ve:
            attempts -= 1
            print("Invalid number entered.")
             
            if attempts > 0:
                print("Invalid.", attempts,
                "attempts remaining...")
            else:
                raise ve

        except ArithmeticError as ar:
            attempts -= 1
            print("Can’t divide by 0.")
             
            if attempts > 0:
                print("Invalid.", attempts,
                "attempts remaining...")
            else:
                raise ar


def login():
    attempts = 4
    while True:
        userid = input("Enter userid: ")
        passwd = input("Enter password: ")
        try:
            validate(userid, passwd)
        except ValueError as ve:
            attempts -= 1
            if attempts > 0:
                print("Invalid.", attempts,
                "attempts remaining...")
            else:
                raise ve 


def guessing_game():   
    number = input("Pick a number: ")
    number = int(number)
    if number < 1 or number > 10:
       raise ValueError ("Invalid guess!, You lost")
    print("You picked:", number)



def numbers(file_name):
    #sum = 0
    #with open(file_name) as a_file:
    try:
        a_file = open(file_name)
    except:
        print('Wrong file name, Please enter the right file name next time')    
        #exit(1)
    for line in a_file:
            try:
                sum = sum + int(line)
            except:
                print("Skipping non-numeric data")

    print ('Sum of numbers = ', sum)


def main():
   
    #my_division()
    #my_file = input('Enter file name ')
    #numbers(my_file)
    test_for_exception()
    #simple_division(6, 0)
    #my_addition()
    #guessing_game()
    '''
    
    my_file = 'f'
    while my_file != 'exit':
        try:
            my_file = input('Enter file name = ')
            numbers(my_file)
        except FileNotFoundError:
            print(my_file,"file name doesn't exist, try again")
        except ValueError:
            print("Trying to add a non-numeric value")
    print('The end')
    '''

main()
