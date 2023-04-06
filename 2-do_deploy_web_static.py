#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ["34.234.204.233", "34.232.69.249"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """distributes archive to servers"""
    try:
        if not (path.exists(archive_path)):
                        return False

        # upload archive
        put(archive_path, '/tmp/')

        # creating target directory
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
                .format(timestamp))
        
        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
    /data/web_static/releases/web_static_{}/'
                .format(timestamp, timestamp))
        
        # removing archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))
        
        # moving contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
    /data/web_static/releases/web_static_{}/'
                .format(timestamp, timestamp))

         # removing the extraneous web_static directory
                run('sudo rm -rf /data/web_static/releases/\
    web_static_{}/web_static'
                    .format(timestamp))

            # delete pre-existing sym link
            run('sudo rm -rf /data/web_static/current')

            # re-establish symbolic link
            run('sudo ln -s /data/web_static/releases/\
    web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # to return True on success
        return True
