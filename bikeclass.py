class Student:
    #mobile = 909
    __slots__ = ['id', 'name', '__credits', '__gpa']
    def __init__(self, id, name, credits, gpa):
        self.id = id
        self.name = name
        self.__credits = credits
        self.__gpa = gpa
        #self.rank = gpa*100 + credits
    
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return self.__gpa

    def get_credits(self):
        return self.__credits

    #This function is to change the gpa for objects
    def set_gpa(self, my_gpa):
        self.__gpa = my_gpa
    
    def set_credits(self, my_credits):
        self.__credits = my_credits

    def __lt__(self, other):
        if type(self) == type(other):
            return self.__credits < other.__credits
        else:
            return False
    
    def __ge__(self, other):
        if type(self) == type(other):
            return self.__credits >= other.__credits
        else:
            return False

class Bike:
    __slots_ = ['__color', '__gears', '__seat', '__training_wheels']
    
    def __init__(self, color, seat):
     self.__color = color
     self.__gears = 21
     self.__seat = seat
     self.__training_wheels = False

    def get_gears(self):
        return self.__gears

    def get_seat(self):
        return self.__seat

    def set_color(self, color):
        self.__color = color   
    
    def set_seat(self, seat):
        self.__seat = seat

    def ride(self, name):
        print(name, "rides their",
        self.__color, "bicycle with",
        self.__gears, "gears and a", 
        self.__seat, "seat!")
        
    def __str__(self):
        return "A " + self.__color + " bike.\n"
    
    def __repr__(self):
        return "Bike:\n  color = " + self.__color \
            + "\n  gears = " + str(self.__gears) \
            + "\n  seat = " + self.__seat \
            + "\n  training wheels = " + \
            str(self.__training_wheels)
    
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__color == other.__color and self.__seat == other.__seat
        else:
            return False   
    
    def __ne__(self, other):
        return not self.__eq__(other)
  
    def __hash__(self):
       return hash(self.__color) * self.__gears


def main():
    
    student1 = Student('200100A', 'Karim', 35, 2.7)
    student2 = Student('200100B', 'Mary', 35, 3.9)
    student3 = Student('8788yu', 'Mohamed', 0, 0)

    '''
    if student1 >= student2:
        print('credits1 >= credits2')
    else:
        print('credits1 < credits2')

    print(type(student1))
    '''

    bike1 = Bike('red', 'leather')
    bike2 = Bike('blue', 'plastic')
    bike3 = Bike('purple', 'soft materials')
    
    print(bike1)

    bike_set = {bike1, bike2, bike3}
    print(bike_set)

    bike_dictionary = {'A':bike1, 'B':bike2, 'C':bike3}

    for key in bike_dictionary:
        print(bike_dictionary[key])


    #bike1.ride('John')
    bike2.set_color('red')
    bike2.set_seat('leather')
    #bike2.ride('Moh')
    #print(bike1.get_seat())
    #bike1.__seat = 'Round'
    #print(bike1.__seat)
    print(type(bike1))
    print(bike1)
    print(bike2)
    
    bicycle = str(bike1)
    #print(bicycle)
    
#    repr(bike1)
    
    if bike1 == bike2:
        print('OK')
    else:
        print('Not OK')
    
    print(bike1 != bike2)

main()

