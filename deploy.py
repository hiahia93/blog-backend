from fabric import Connection
import os
import argparse
import time

REMOTE_WORK = '/root/app/compose/blogback'
REPO = 'jianjiago/blogback'


def local(repo):
    os.system('docker build -t blogback:latest .')
    os.system('docker tag blogback {0}'.format(repo))
    os.system('docker push {0}'.format(repo))


def remote(repo):
    conn = Connection(host='94.191.3.181', user='root', connect_kwargs={
        'key_filename': '/home/edgar/Documents/centos_tencent.key'
    })
    with conn.cd(REMOTE_WORK):
        conn.run('docker pull {0}'.format(repo))
        conn.run('docker-compose -f blogback.yml stop')
        conn.run('docker-compose -f blogback.yml rm -f')
        conn.put('blogback.yml', REMOTE_WORK)
        conn.put('nginx.conf', REMOTE_WORK)
        conn.put('blog.sql', REMOTE_WORK)
        conn.run('docker-compose -f blogback.yml up -d')


if __name__ == '__main__':
    start = int(time.time())
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', default='dev', type=str)
    args = parser.parse_args()
    repo = '{0}:{1}'.format(REPO, args.t)
    local(repo)
    remote(repo)
    print(int(time.time() - start))
