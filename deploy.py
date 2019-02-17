from configparser import ConfigParser

from fabric import Connection
import os
import argparse

REMOTE_WORK = '/root/app/blog-backend'
REPO = 'jianjiago/blogback'


def local(commit_message):
    os.system('./push.sh "{0}"'.format(commit_message))


def remote(repo, push):
    cf = ConfigParser()
    cf.read("./config-private.ini")
    conn = Connection(host=cf.get('remote', 'ip'), user='root', connect_kwargs={
        'key_filename': './amd_centos'
    })
    with conn.cd(REMOTE_WORK):
        conn.run('docker-compose stop')
        conn.run('docker-compose rm -f')
        conn.run('git pull origin master')
        conn.run('docker build -t {0} .'.format(repo))
        conn.run('docker-compose up -d')
        if push:
            conn.run('docker push {0}'.format(repo))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default='modified something', type=str)
    parser.add_argument('-t', default='dev', type=str)
    # Whether push the image to your personal docker hub, default is no.
    parser.add_argument('-p', default='n', type=str)
    args = parser.parse_args()
    repo = '{0}:{1}'.format(REPO, args.t)
    local(args.m)
    push = args.p != 'n'
    remote(repo, push)
