import datetime
import requests


def find_questions():
    url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
    today = datetime.datetime.today()
    unix_today = int(today.timestamp())
    unix_from_day = int((today - datetime.timedelta(2)).timestamp())
    params = {
        'order': 'desc',
        'sort': 'activity',
        'fromdate': unix_from_day,
        'today': unix_today,
        'tagged': 'python'
    }
    response = requests.get(url, params=params).json()['items']
    for i, item in enumerate(response):
      print(f'{i + 1}. {item["title"]}')


find_questions()