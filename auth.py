import requests

url = "http://localhost:3000/api/session"


class UserData:
    username: str
    password: str
    remember: bool


userData: UserData = {
    "username": "adars@gmail.com",
    "password": "adars@123",
    "remember": True,
}


def login_user(user_data: UserData = userData):
    res = requests.post(url=url, json=user_data)

    if res.status_code == 200:
        print("User logged in successfully!")
        return res.json()
    else:
        print("User credentials not valid!")
        return None


if __name__ == "__main__":
    data = login_user()
    print(data)
