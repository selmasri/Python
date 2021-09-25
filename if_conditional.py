
def decision_making(grade):
    if grade >= 90:
        print("Excellent, grade = ", grade)
        return grade
    elif grade >= 80 and grade <90:
        print("Good, grade = ", grade)
    elif grade > 50 and grade < 60:
        print("Fail, grade = ", grade)
    else:
        print("Retake exam, grade = ", grade)
 
 #   else:
 #       print("Print distance if it's not zero or greater than 15 =", distance)
    
 #   distance = distance + 6
 #   print("Distance =", distance)



def main():
    dist = int(input("Enter grade = "))
    print(decision_making(dist))
    #print("sam = ", sam)

main()