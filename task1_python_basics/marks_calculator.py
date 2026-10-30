# Task 1 - Student marks calculator


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")
    subjects = int(input("How many subjects? "))

    total = 0
    for i in range(1, subjects + 1):
        marks = float(input("Marks for subject " + str(i) + " (out of 100): "))
        while marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            marks = float(input("Enter marks again: "))
        total = total + marks

    percentage = total / subjects
    grade = get_grade(percentage)

    print("\n--- Result for", name, "---")
    print("Total marks:", total, "out of", subjects * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    if grade == "F":
        print("Result: Fail")
    else:
        print("Result: Pass")


main()
