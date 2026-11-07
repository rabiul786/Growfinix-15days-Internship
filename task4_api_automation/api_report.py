# Task 4 - Get data from a public API and make a CSV report
import requests
import pandas as pd

USERS_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def get_data(url):
    # Calls the API and returns the JSON data (or None if something goes wrong)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print("Could not get data from", url)
        print("Error:", error)
        return None


def main():
    users = get_data(USERS_URL)
    posts = get_data(POSTS_URL)

    if users is None or posts is None:
        print("Report not created because the API call failed.")
        return

    users_df = pd.DataFrame(users)
    posts_df = pd.DataFrame(posts)

    # Count how many posts each user has written
    post_counts = posts_df.groupby("userId").size().reset_index(name="post_count")

    # Join the user details with their post count
    report = users_df[["id", "name", "email"]].merge(
        post_counts, left_on="id", right_on="userId"
    )
    report = report[["id", "name", "email", "post_count"]]

    report.to_csv("user_report.csv", index=False)
    print(report)
    print("\nReport saved as user_report.csv")


main()
