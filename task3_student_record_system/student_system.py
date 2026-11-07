# Task 3 - Student Record Management System (Python + SQLite)
import sqlite3


class Student:
    def __init__(self, roll_no, name, age, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


def connect_db():
    conn = sqlite3.connect("students.db")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS students (
            roll_no TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            course TEXT,
            marks REAL
        )"""
    )
    conn.commit()
    return conn


def print_rows(rows):
    if len(rows) == 0:
        print("No records found.")
        return
    print("\nRoll No   Name          Age   Course      Marks")
    print("-" * 52)
    for row in rows:
        print(str(row[0]).ljust(9), str(row[1]).ljust(13), str(row[2]).ljust(5),
              str(row[3]).ljust(11), row[4])


def add_student(conn):
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    course = input("Enter course: ").strip()
    marks = float(input("Enter marks: "))

    student = Student(roll_no, name, age, course, marks)
    try:
        conn.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                     (student.roll_no, student.name, student.age, student.course, student.marks))
        conn.commit()
        print("Student added.")
    except sqlite3.IntegrityError:
        print("This roll number already exists.")


def view_students(conn):
    rows = conn.execute("SELECT * FROM students").fetchall()
    print_rows(rows)


def search_student(conn):
    keyword = input("Enter name or roll number to search: ").strip()
    rows = conn.execute(
        "SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ?",
        ("%" + keyword + "%", "%" + keyword + "%"),
    ).fetchall()
    print_rows(rows)


def update_student(conn):
    roll_no = input("Enter roll number to update: ").strip()
    row = conn.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,)).fetchone()
    if row is None:
        print("Student not found.")
        return

    print("Press Enter to keep the old value.")
    name = input("New name (" + row[1] + "): ").strip() or row[1]
    age = input("New age (" + str(row[2]) + "): ").strip() or row[2]
    course = input("New course (" + row[3] + "): ").strip() or row[3]
    marks = input("New marks (" + str(row[4]) + "): ").strip() or row[4]

    conn.execute("UPDATE students SET name=?, age=?, course=?, marks=? WHERE roll_no=?",
                 (name, int(age), course, float(marks), roll_no))
    conn.commit()
    print("Student updated.")


def delete_student(conn):
    roll_no = input("Enter roll number to delete: ").strip()
    cursor = conn.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Student not found.")
    else:
        print("Student deleted.")


def main():
    conn = connect_db()
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student(conn)
            elif choice == "2":
                view_students(conn)
            elif choice == "3":
                search_student(conn)
            elif choice == "4":
                update_student(conn)
            elif choice == "5":
                delete_student(conn)
            elif choice == "6":
                print("Bye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Age and marks must be numbers.")

    conn.close()


main()
