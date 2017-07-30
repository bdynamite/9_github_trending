import requests
import datetime

TOP_SIZE = 3
DAYS = 7
REPO_URL = 'https://api.github.com/search/repositories'
ISSUE_URL = 'https://api.github.com/repos/{}/{}/issues'


def get_time():
    n_days_ago = datetime.datetime.today() - datetime.timedelta(days=DAYS)
    return n_days_ago.strftime('%Y-%m-%d')


def get_trending_repositories(top_size):
    params = {
        'q': 'created:>{}'.format(get_time()),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    responce = requests.get(url=REPO_URL, params=params)
    return [Repository(x) for x in responce.json()['items']]

class Repository:

    def __init__(self, params_dict):
        self.url = params_dict['html_url']
        self.name = params_dict['name']
        self.owner = params_dict['owner']['login']
        self.issues = get_open_issues_amount(self.owner, self.name)

    def __repr__(self):
        return 'Repository "{}"'.format(self.name)

    def print_with_issues(self):
        print('*'*20)
        print(self)
        print('url: {}'.format(self.url))
        print('issues: {}'.format(len(self.issues)))
        print('\n'.join(['{} {}'.format(x['title'], x['url']) for x in self.issues]))


def get_open_issues_amount(repo_owner, repo_name):
    responce = requests.get(url=ISSUE_URL.format(repo_owner, repo_name))
    return responce.json()

if __name__ == '__main__':
    repositories = get_trending_repositories(TOP_SIZE)
    [x.print_with_issues() for x in sorted(repositories, key= lambda x: len(x.issues))]
