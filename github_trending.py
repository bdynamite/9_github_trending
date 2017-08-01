import requests
import datetime
from collections import namedtuple

repository = namedtuple('Repository', 'url name owner issues')


def get_time():
    n_days_ago = datetime.datetime.today() - datetime.timedelta(days=7)
    return n_days_ago.strftime('%Y-%m-%d')


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:>{}'.format(get_time()),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    responce = requests.get(url=url, params=params)
    return [repository(url=x['html_url'],
                       name=x['name'],
                       owner=x['owner']['login'],
                       issues=get_open_issues_amount(x['owner']['login'], x['name']))
            for x in responce.json()['items']]


def print_repos(repositories):
    for repo in sorted(repositories, key=lambda x: len(x.issues)):
        print('*' * 20)
        print('Repository "{}"'.format(repo.name))
        print('url: {}'.format(repo.url))
        print('issues: {}'.format(len(repo.issues)))
        print('\n'.join(['{} {}'.format(x['title'], x['url']) for x in repo.issues]))


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'
    responce = requests.get(url=url.format(repo_owner, repo_name))
    return responce.json()

if __name__ == '__main__':
    repositories = get_trending_repositories(20)
    print_repos(repositories)