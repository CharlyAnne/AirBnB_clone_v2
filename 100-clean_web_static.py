#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *
import os

env.hosts = ["34.234.204.233", "34.232.69.249"]
env.user = "ubuntu"


def do_clean(number=0):
   """Delete out-of-date archives.
   
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    if number == 0:
        numbers = 1
    else:
        numbers = number

    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(numbers))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, numbers))
