import requests
from auth import login_user, UserData
from user import get_current_user

url = "http://localhost:3000/api/database"

json_data = {
    "is_on_demand": False,
    "is_full_sync": True,
    "is_sample": False,
    "cache_ttl": None,
    "refingerprint": False,
    "auto_run_queries": True,
    "schedules": {},
    "details": {
        "host": "host.docker.internal",
        "port": 5432,
        "dbname": "staging_sept_23",
        "user": "postgres",
        "use-auth-provider": False,
        "password": "demo#1234k",
        "schema-filters-type": "all",
        "ssl": False,
        "tunnel-enabled": False,
        "advanced-options": False,
    },
    "name": "varicon-db",
    "engine": "postgres",
}

userData: UserData = {
    "username": "adars@gmail.com",
    "password": "adars@123",
    "remember": True,
}

login = login_user(userData)
current = get_current_user(login["id"])

cookies = {"metabase.SESSION": login["id"], "metabase.TIMEOUT": "alive"}

response = requests.post(url=url, json=json_data, cookies=cookies)

if response.status_code == 200:
    print("Success")

    data = response.json()
    print(data)
else:
    print("Some error occured!")
    print(response.text)
