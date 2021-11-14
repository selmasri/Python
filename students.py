class Student:
    #mobile = 909
    __slots__ = ['id', 'name', '__credits', '__gpa']
    def __init__(self, id, name, credits, gpa):
        self.id = id
        self.name = name
        self.__credits = credits
        self.__gpa = gpa
        #self.rank = gpa*100 + credits
    
    def get_gpa(self):
        return self.__gpa

    def get_credits(self):
        return self.__credits

    def set_gpa(self, my_gpa):
        self.__gpa = my_gpa
    
    def set_credits(self, my_credits):
        self.__credits = my_credits


    '''
    id = 'No ID'
    name = 'Student'
    credits = 0
    #hard_drive = 0 # hard drive in GB 
    #ram = 0 # size of the ram in GB
    gpa = 0.0   #Great Point Average
    address = 'No address'
    phone_number = 0
    '''
# This function is to print all features of the objects
#def print_student(a_student):
#    print(a_student.id, a_student.name, a_student.credits, a_student.gpa)

def main():
    student1 = Student('200100A', 'Karim', 25, 3.7)
    student2 = Student('200100B', 'Mary', 15, 2.9)
    student3 = Student('8788yu', 'Mohamed', 0, 0)
    #print_student(student1)
    
    print("Student1's gpa = ", student1.get_gpa())
    print("Student2's credits = ", student2.get_credits())
    
    student1.set_gpa(4)
    student2.set_credits(40)
    
    print("Student1's gpa = ", student1.get_gpa())
    print("Student2's credits = ", student2.get_credits())
   
    #student1.__gpa = 4
    #print_student(student1)
    #print(student1.phone)

    #print_student(student2)
    #print_student(student3)
    #student3.phone = 989898
    #print(student3.phone)
    #print(student1.phone)
    #student4 = Student()
    '''
    print_student(student3)
    #student1.address ='Dubai'
    #print(student1.phone)
    print(student1.mobile)
    print(student2.mobile)
    print(student3.mobile)
    print(Student.mobile)
    '''
    '''
    student1 = Student()
    student2 = Student()
    student3 = Student()

    print_student(student1)
    print_student(student2)
    
    student1.id = '200100AC'
    student1.name = 'Karim'
    student1.credits = 25
    student1.gpa = 3.8
    student2.name = 'Dana'
    student2.address = '34 Erie St., Silicon Oasis, Dubai, UAE'
    student2.phone_number = 576986908
    print_student(student1)
    print_student(student2)
    '''
main()