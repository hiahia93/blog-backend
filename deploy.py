from configparser import ConfigParser

from fabric import Connection
import os
import argparse

REMOTE_WORK = '/root/app/blog-backend'
REPO = 'jianjiago/blogback'


def local(repository):
    os.system('docker-compose stop')
    os.system('docker-compose rm -f')
    os.system('docker build -t {0} .'.format(repository))
    os.system('docker-compose up')


def remote(repository, commit_message):
    cf = ConfigParser()
    cf.read("./config-private.ini")
    conn = Connection(host=cf.get('remote', 'ip'), user='root', connect_kwargs={
        'key_filename': './amd_centos'
    })
    os.system('./script/push.sh "{0}"'.format(commit_message))

    with conn.cd(REMOTE_WORK):
        conn.run('docker-compose stop')
        conn.run('docker-compose rm -f')
        conn.run('git pull origin master')
        conn.run('docker build -t {0} .'.format(repository))
        conn.run('docker-compose up -d')
        conn.run('docker push {0}'.format(repository))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default='modified something', type=str)
    parser.add_argument('-t', default='dev', type=str)
    # Whether deploy the app to the remote server, default is no.
    parser.add_argument('-d', default='n', type=str)
    args = parser.parse_args()
    repo = '{0}:{1}'.format(REPO, args.t)
    deploy = args.d != 'n'
    if deploy:
        remote(repo, args.m)
    else:
        local(repo)
