# Task 2 - Student details using dictionaries and files (text, CSV, JSON)
import csv
import json

JSON_FILE = "students.json"
CSV_FILE = "students.csv"
TEXT_FILE = "students.txt"

# Dictionary where key = roll number and value = another dictionary of details
students = {}


def add_student():
    roll_no = input("Enter roll number: ").strip()
    if roll_no == "":
        print("Roll number cannot be empty.")
        return
    if roll_no in students:
        print("This roll number already exists.")
        return

    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip()

    if not age.isdigit():
        print("Age must be a number.")
        return

    students[roll_no] = {"name": name, "age": int(age), "course": course}
    print("Student added.")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return
    print("\nRoll No   Name        Age   Course")
    print("-" * 40)
    for roll_no in students:
        s = students[roll_no]
        print(roll_no.ljust(10), s["name"].ljust(11), str(s["age"]).ljust(5), s["course"])


def save_to_json():
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)
    print("Saved to", JSON_FILE)


def load_from_json():
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        students.update(data)
        print("Loaded", len(data), "student(s) from", JSON_FILE)
    except FileNotFoundError:
        print("No saved file found. Starting fresh.")
    except json.JSONDecodeError:
        print("The JSON file is damaged. Starting fresh.")


def save_to_csv():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["roll_no", "name", "age", "course"])
        for roll_no in students:
            s = students[roll_no]
            writer.writerow([roll_no, s["name"], s["age"], s["course"]])
    print("Saved to", CSV_FILE)


def save_to_text():
    with open(TEXT_FILE, "w") as file:
        for roll_no in students:
            s = students[roll_no]
            file.write(roll_no + ", " + s["name"] + ", " + str(s["age"]) + ", " + s["course"] + "\n")
    print("Saved to", TEXT_FILE)


def main():
    load_from_json()
    while True:
        print("\n--- Student Manager ---")
        print("1. Add student")
        print("2. View students")
        print("3. Save to JSON")
        print("4. Save to CSV")
        print("5. Save to text file")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            save_to_json()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            save_to_text()
        elif choice == "6":
            save_to_json()
            print("Bye!")
            break
        else:
            print("Invalid choice.")


main()
