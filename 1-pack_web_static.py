#!/usr/bin/python3
"""
a fabric script that generates a .tgz archive
from the contents of web_static folder
"""
from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
    """generates the .tgz archive from a folder"""
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
