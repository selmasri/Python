def make_student(id, name):
    credits = 0
    gpa = 0

    return id, name, credits, gpa
'''
def add_student(id, name):
    population = [(100200, 'Karim', 0, 0), (100300, 'Sam', 0, 0)]
    for index in range(len(population)):
        if population:
'''
def fdict():
    a_dict = dict()
    b_dict = {}
    c_dict = {'ID':100300, 'name':'Samir', 'Credit':24, 'GPA':3.5}
    c_dict['address'] = 'Marina - Dubai'

    print(c_dict)
def names():
    names = dict()
    names['S'] = 'Samir'
    names['D'] = 'Diab'
    names['E'] = 'El-Masri'
    names['E'] = 'Elhadi'
    print(names)
    print(names['E'])

def more_dict():
    a_dict = {"one":1, "two":2}
    value = a_dict["two"]
    print(value)
    value = a_dict["bad key"]

def check_first(a_dict, key):
    if key in a_dict:
        #print(value)
        value = a_dict[key]
        print(value)

def print_dict(a_dict):
    for key in a_dict:
        value = a_dict[key]
        print(key, ':', value)
    new_list = sorted(a_dict.keys())
    print(new_list)

def add_student(a_dict, id, name, credit = 0, gpa = 0):


def main():
    c_dict = { 'ID':100300, 'name':'Samir', 'Credits':24, 'GPA':3.5}
    id = 100400
    name = 'Karim'
    add_student(c_dict, id, name)

    #check_first(c_dict, 'GPA')
    #print_dict(c_dict)
    #more_dict()
    #names()
    #fdict()

    '''
    student1 = make_student(100200, "Karim")
    student2 =make_student(100201, "Mary")
    student3 =make_student(100202, "Mohammad")
    student4 =make_student(100203, "John")
    print(student1)
    print(student2)
    print(student3)
    print(student4)

    population = {}
    print(type(population))
    '''

main()