from git import Repo
from datetime import datetime

def was_it_rufus(git_dir):
    repo = Repo(git_dir)
    
    print('active branch: ', repo.git.status().split('\n')[0][10:], '\n')
    print('local changes: ', repo.is_dirty(), '\n')

    today = datetime.today()
    today_timestamp = datetime.timestamp(today)
    pre7_timestamp = today_timestamp - 604800 # a week

    commits_list = list(repo.iter_commits())
    last_commit = commits_list[0]
    if last_commit.committed_date>=pre7_timestamp:
        print('recent commit: True\n')
    else:
        print('recent commit: False\n')
    if last_commit.author.name == 'Rufus':
        print('blame Rufus: True\n')
    else:
        print('blame Rufus: False\n')
