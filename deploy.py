from fabric import Connection
import os
import argparse
import time

REMOTE_WORK = '/root/app/blog-backend'
REPO = 'jianjiago/blogback'


def local(commit_message):
    os.system("./push.sh {0}".format(commit_message))


def remote(repo):
    conn = Connection(host='94.191.3.181', user='root', connect_kwargs={
        'key_filename': '/home/edgar/Documents/centos_tencent.key'
    })
    with conn.cd(REMOTE_WORK):
        conn.run('docker-compose stop')
        conn.run('docker-compose rm -f')
        conn.run('git pull origin master')
        conn.run('docker build -t {0} .'.format(repo))
        conn.run('docker-compose up -d')
        conn.run('docker push {0}'.format(repo))


if __name__ == '__main__':
    start = int(time.time())
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default='modified something', type=str)
    parser.add_argument('-t', default='dev', type=str)
    args = parser.parse_args()
    repo = '{0}:{1}'.format(REPO, args.t)
    local(args.m)
    remote(repo)
