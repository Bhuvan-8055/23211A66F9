import requests
from datetime import datetime

API_URL = "http://4.224.186.213/evaluation-service/vehicles"

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiIyMzIxMWE2NmY5QGJ2cml0LmFjLmluIiwiZXhwIjoxNzgyMzgzMTEzLCJpYXQiOjE3ODIzODIyMTMsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI4OGZiOWI1My0yZTBlLTQ5OTYtYTFkMy1mYjg1MWE1NWVkMWYiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJzcmkgYmh1dmFuIHBhbmRpcmkiLCJzdWIiOiJiYmU2MDcwNy00YmU0LTRmOTMtYjY1MC1iMmYyNGIzN2I4ZjEifSwiZW1haWwiOiIyMzIxMWE2NmY5QGJ2cml0LmFjLmluIiwibmFtZSI6InNyaSBiaHV2YW4gcGFuZGlyaSIsInJvbGxObyI6IjIzMjExYTY2ZjkiLCJhY2Nlc3NDb2RlIjoiYWhYanZwIiwiY2xpZW50SUQiOiJiYmU2MDcwNy00YmU0LTRmOTMtYjY1MC1iMmYyNGIzN2I4ZjEiLCJjbGllbnRTZWNyZXQiOiJNVFBkdXJOeGVIS2N0SGV0In0.ypzzpZCFtR-d4Q-RWWo_R1NQNxcAbin57P8mbWp6Pe"

TYPE_WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}


def calculate_score(notification):
    weight = TYPE_WEIGHT.get(notification["Type"], 0)

    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    return (weight, timestamp)


def fetch_notifications():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }

    response = requests.get(API_URL, headers=headers)

    print("Status Code:", response.status_code)

    response.raise_for_status()

    data = response.json()

    return data.get("notifications", [])


def get_top_notifications(notifications, limit=10):
    notifications.sort(
        key=calculate_score,
        reverse=True
    )

    return notifications[:limit]


def display_notifications(notifications):
    print("\n========== TOP 10 PRIORITY NOTIFICATIONS ==========\n")

    for i, notification in enumerate(notifications, start=1):
        print(f"{i}.")
        print(f"ID        : {notification['ID']}")
        print(f"Type      : {notification['Type']}")
        print(f"Message   : {notification['Message']}")
        print(f"Timestamp : {notification['Timestamp']}")
        print("-" * 50)


def main():
    try:
        notifications = fetch_notifications()

        if not notifications:
            print("No notifications found.")
            return

        top_notifications = get_top_notifications(notifications)

        display_notifications(top_notifications)

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()