from fabric.api import *

env.hosts = ['ubuntu@34.234.204.233', 'ubuntu@34.232.69.249']

def copy():
    put('0-setup_web_static.sh', '~/')
