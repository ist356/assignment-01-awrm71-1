'''
This program takes a gpa as input and returns one of the following:

    "Invalid GPA" when gpa is outside the 0.0 to 4.0 range
    "Summa Cum Laude" when gpa >= 3.8
    "Magna Cum Laude" when gpa >= 3.6 and gpa < 3.8
    "Cum Laude" when gpa >=3.4 and gpa < 3.6
    "Academic Probation" when gpa <= 1.8
    "Passing" for any other gpa


Please note this program was written incorrectly on purpose. You will learn to use
pytest to identify non-error bugs in your code.

'''

gpa = float(input("Enter GPA: "))

if gpa >=0 and gpa <= 4.0:
    if gpa >= 3.8:
        result = "Summa Cum Laude"
    elif gpa >= 3.6:
        result = "Magna Cum Laude"
    elif gpa >= 3.4:
        result = "Cum Laude"
    elif gpa <= 1.8:
        result = "Academic Probation"
    else:
        result = "Passing"
else:
    result = "Invalid GPA"

print(f"for GPA {gpa:.3f} Result: {result}")



if __name__ == "__main__":
    main()


"""
implimenting the code itself was very easy for both the tests, the big thing that I learned was the way that tests opperate. While the code itself is easy I think the functionality of tests and debugging is very interesting and a new perspective into coding."""



