# Task 4: Python Automation and API Integration

This script gets users and posts from a free public API ([JSONPlaceholder](https://jsonplaceholder.typicode.com)), counts the posts written by each user with Pandas and saves a CSV report.

## How to run

```
pip install requests pandas
python api_report.py
```

## What it does

1. Sends GET requests with the `requests` library
2. Handles errors like no internet or a bad response using `try/except`
3. Converts the JSON data into Pandas DataFrames
4. Counts posts per user and joins it with the user details
5. Saves `user_report.csv`

## Sample output

```
   id                      name                      email  post_count
0   1             Leanne Graham          Sincere@april.biz          10
1   2              Ervin Howell          Shanna@melissa.tv          10
...
Report saved as user_report.csv
```
