import os
import requests
from dotenv import load_dotenv
from auth import login_user
from user import get_current_user

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

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
        "host": DB_HOST,
        "port": DB_PORT,
        "dbname": DB_NAME,
        "user": DB_USER,
        "use-auth-provider": False,
        "password": DB_PASS,
        "schema-filters-type": "all",
        "ssl": False,
        "tunnel-enabled": False,
        "advanced-options": False,
    },
    "name": "varicon-db",
    "engine": "postgres",
}

login = login_user()
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
