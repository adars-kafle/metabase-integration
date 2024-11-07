import requests
from auth import login_user

url = "http://localhost:3000/api/user/current"


def get_current_user(id: str | None = None):
    cookies = {}
    if id:
        cookies.update({"metabase.SESSION": id, "metabase.TIMEOUT": "alive"})

    res = requests.get(url=url, cookies=cookies)
    if res.status_code == 200:
        print("User logged in!")
        return res.json()
    else:
        print("Please login to continue!")
        return None


if __name__ == "__main__":
    login = login_user()
    current_user = get_current_user(login["id"])
    print(current_user)
