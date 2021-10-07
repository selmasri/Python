import csv
import re

def open_csv():
    with open("song\customers.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        #skip the header row
        #next(csv_reader)
        # iterate over the records
        for record in csv_reader:
            print(record[0], ' - ', record[1], ' - ', record[2], ' - ', record[3]) # Name
            #print(record[1]) # address
            #print(record[2]) # address


def find_digits(a_str):
    #for match in re.findall("23", a_str):
    for match in re.findall('\d', a_str):
        print(match)


def str_search():
    for match in re.findall("\d\D", "1ab23#lkmh"):
        print(match)
        if re.findall("\d[a-z]", "1ab23c"):
            print("Found at least one match!")
        else:
            print("No match!")




def main():
    #find_digits('2.56')
    #open_csv()
    str_search()

main()