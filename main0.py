import csv


def get_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    else:
        return "D"

with open("data.csv","r") as file:
    reader=csv.reader(file)
    next(reader) #which skips the header

    for row in reader:
        name=row[1]
        marks=list(map(int,row[1:]))

        average=sum(marks)/len(marks)
        highest=max(marks)
        lowest=min(marks)
        grade=get_grade(average)
        #printing each students individually
        print("Name:", name)
        print("Grade:", grade)
        print("Average:", round(average,2))
        print("Lowest:", lowest)
        print("Highest:", highest)
        print("---------------------------------------") 