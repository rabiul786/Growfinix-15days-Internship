# Task 5: Testing, Improvement and Final Project

This is the final version of the Student Record Management System from Task 3. I added input checking, better error messages and unit tests with pytest.

## What was improved

- Roll number, name, age, course and marks are checked before saving
- Clear error messages instead of the program crashing
- Duplicate roll numbers are not allowed
- Updating or deleting a student that does not exist gives an error
- New feature: average marks
- 19 test cases written with pytest

## Files

- `student_system.py` - the main program
- `test_student_system.py` - the tests

## How to run

```
pip install pytest
python student_system.py
```

## How to run the tests

```
pytest
```

## Cases tested

- age that is text, negative, too small or too big
- marks below 0, above 100 or not a number
- empty name or a name with numbers
- duplicate roll number
- search with an empty word
- a SQL injection attempt in the search box
- update and delete for a student who is not in the database
- average marks when there are no students

## Sample output

```
Student added.
Student added.
Error: Age must be a number between 3 and 100.

Roll No   Name          Age   Course      Marks
----------------------------------------------------
101       Rahim Khan    20    B.Tech      82.5
102       Ayesha Begum  21    B.Sc        91.0
Average marks: 86.75
```


