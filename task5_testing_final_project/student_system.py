# Task 5 - Final project: Student Record Management System
# Same as Task 3 but with input validation, error handling and tests.
import sqlite3


def connect_db(db_name="students.db"):
    conn = sqlite3.connect(db_name)
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


# ---------- validation functions ----------
def is_valid_roll_no(roll_no):
    return roll_no.isalnum() and len(roll_no) <= 15


def is_valid_name(name):
    return name.replace(" ", "").isalpha()


def is_valid_age(age):
    return str(age).isdigit() and 3 <= int(age) <= 100


def is_valid_marks(marks):
    try:
        return 0 <= float(marks) <= 100
    except ValueError:
        return False


def check_all(roll_no, name, age, course, marks):
    # Raises ValueError with a clear message if any input is wrong
    if not is_valid_roll_no(roll_no):
        raise ValueError("Roll number must have only letters/numbers (max 15).")
    if not is_valid_name(name):
        raise ValueError("Name must contain only letters and spaces.")
    if not is_valid_age(age):
        raise ValueError("Age must be a number between 3 and 100.")
    if course.strip() == "":
        raise ValueError("Course cannot be empty.")
    if not is_valid_marks(marks):
        raise ValueError("Marks must be a number between 0 and 100.")


# ---------- database functions ----------
def get_student(conn, roll_no):
    return conn.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,)).fetchone()


def add_student(conn, roll_no, name, age, course, marks):
    roll_no = roll_no.strip()
    name = name.strip()
    course = course.strip()
    check_all(roll_no, name, age, course, marks)

    if get_student(conn, roll_no) is not None:
        raise ValueError("This roll number already exists.")

    conn.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                 (roll_no, name, int(age), course, float(marks)))
    conn.commit()


def get_all_students(conn):
    return conn.execute("SELECT * FROM students ORDER BY roll_no").fetchall()


def search_students(conn, keyword):
    keyword = keyword.strip()
    if keyword == "":
        raise ValueError("Search word cannot be empty.")
    like = "%" + keyword + "%"
    return conn.execute(
        "SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ? OR course LIKE ?",
        (like, like, like),
    ).fetchall()


def update_student(conn, roll_no, name, age, course, marks):
    if get_student(conn, roll_no) is None:
        raise ValueError("Student not found.")
    name = name.strip()
    course = course.strip()
    check_all(roll_no, name, age, course, marks)

    conn.execute("UPDATE students SET name=?, age=?, course=?, marks=? WHERE roll_no=?",
                 (name, int(age), course, float(marks), roll_no))
    conn.commit()


def delete_student(conn, roll_no):
    if get_student(conn, roll_no) is None:
        raise ValueError("Student not found.")
    conn.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()


def average_marks(conn):
    result = conn.execute("SELECT AVG(marks) FROM students").fetchone()[0]
    if result is None:
        return 0
    return round(result, 2)


# ---------- menu ----------
def print_rows(rows):
    if len(rows) == 0:
        print("No records found.")
        return
    print("\nRoll No   Name          Age   Course      Marks")
    print("-" * 52)
    for row in rows:
        print(str(row[0]).ljust(9), str(row[1]).ljust(13), str(row[2]).ljust(5),
              str(row[3]).ljust(11), row[4])


def main():
    conn = connect_db()
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Show average marks")
        print("7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student(conn, input("Roll number: "), input("Name: "), input("Age: "),
                            input("Course: "), input("Marks: "))
                print("Student added.")
            elif choice == "2":
                print_rows(get_all_students(conn))
            elif choice == "3":
                print_rows(search_students(conn, input("Search word: ")))
            elif choice == "4":
                update_student(conn, input("Roll number to update: ").strip(), input("New name: "),
                               input("New age: "), input("New course: "), input("New marks: "))
                print("Student updated.")
            elif choice == "5":
                delete_student(conn, input("Roll number to delete: ").strip())
                print("Student deleted.")
            elif choice == "6":
                print("Average marks:", average_marks(conn))
            elif choice == "7":
                print("Bye!")
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print("Error:", error)

    conn.close()


if __name__ == "__main__":
    main()
