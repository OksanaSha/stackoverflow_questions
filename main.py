import requests

from datetime import datetime


def get_params(from_date, to_date, tags):
    '''
    :param from_date: 'YYYY-MM-DD'
    :param to_date: 'YYYY-MM-DD'
    :param tags: ['tag1', 'tag2', ...]
    :return: params
    '''
    from_year, from_month, from_day = [int(val) for val in from_date.split('-')]
    to_year, to_month, to_day = [int(val) for val in to_date.split('-')]
    from_date_unix = int(datetime(from_year, from_month, from_day).timestamp())
    to_date_unix = int(datetime(to_year, to_month, to_day).timestamp())

    params = {
        'site': 'stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'page': 1,
        'fromdate': from_date_unix,
        'todate': to_date_unix,
        'tags': tags
    }
    return params

params = get_params('2021-10-07', '2021-10-09', ['Python'])
page = 1

while True:
    params['page'] = f'{page}'
    response = requests.get('https://api.stackexchange.com/questions', params=params)
    response_json = response.json()

    with open('questions.txt', 'a') as file:
        for item in response_json['items']:
            file.write(item['title'])
            file.write('\n')

    if response_json['has_more']:
        page += 1
    else:
        print ('Success')
        break