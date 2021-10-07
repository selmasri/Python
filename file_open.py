
# open the "input.txt" file in the 
# "data" subdirectory using a
# relative path.
def print_lines(file_name):
    
    my_file = open(file_name)
    # use a for loop to print the length
    # of each line
    
    for line in my_file:
        line1 = line.strip()
        tokens = line1.split(",")
        print(tokens[0], tokens[1], tokens[2])
        #my_file.close()
        #length = len(line)
        #print(length)
    
    """
    for line in my_file:
        line = line.strip()
        tokens = line.split(" ")
        
        for token in tokens:
            if token == word:
                print(token)
        #print(tokens)
        #print(tokens[0], tokens[1], tokens[2])
        
         
        for token in tokens:
            if token == word:
                print(token)
    """
        #print(line)
        #print(line, end="")
        #print(line.strip())

    my_file.close()

def auto_file():
    with open("song\me.txt") as a_file:
        for line in a_file:
            stripped = line.strip()
            print(stripped)



def write_to_file():
    name = input("Enter name: ")
    a_file = open("a_file.txt", "w")
    a_file.write(str(25))
    a_file.write('\n')
    a_file.write(name)




def main():
    #word_search = input("Enter the word to search ")
    #print_lines("song\me.txt", word_search)
    #print_lines("my_file.csv")
    write_to_file()
    #auto_file()

main()