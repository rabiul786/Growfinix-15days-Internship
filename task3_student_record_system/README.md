# Task 3: Student Record Management System

A menu-based program to **add, view, search, update and delete** student records. The data is saved in an SQLite database (`students.db`), which is created automatically.

## How to run

```
python student_system.py
```

## Database table

| Column | Type |
|---|---|
| roll_no | TEXT (primary key) |
| name | TEXT |
| age | INTEGER |
| course | TEXT |
| marks | REAL |

## Sample output

```
Roll No   Name          Age   Course      Marks
----------------------------------------------------
101       Rahim         20    B.Tech      82.5
102       Ayesha        21    B.Sc        91.0
```

## Things used

- `Student` class to hold one student's details
- functions for each operation
- SQL queries with `?` placeholders
- `try/except` for wrong input and duplicate roll numbers
