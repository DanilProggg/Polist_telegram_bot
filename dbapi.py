import requests
import datetime
from entity.User import User

url = "http://10.12.131.11:8080"


def get_today_day(user: User):
    today = datetime.date.today()
    params = {'id': user.group, 'date': today}
    r = requests.get(url + "/api/v1/pare/bygroup-and-date", params=params)
    return r


def get_tomorrow_day(user: User):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    params = {'id': user.group, 'date': tomorrow}
    r = requests.get(url + "/api/v1/pare/bygroup-and-date", params=params)
    print(r.headers)
    print(r.url)
    return r


def get_after_tomorrow_day(user: User):
    tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    params = {'id': user.group, 'date': tomorrow}
    r = requests.get(url + "/api/v1/pare/bygroup-and-date", params=params)
    print(r.headers)
    print(r.url)
    return r


def get_group_id_by_name(name):
    params = {'name': name}
    r = requests.get(url + "/api/v1/group/getIdByName", params=params)
    print(r.headers)
    print(r.url)
    return r

