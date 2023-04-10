#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the content of webstatic
# folder of the AirBnB clone repo using do_pack

from fabric.api import local


def list_l():
    local("ls -l")
