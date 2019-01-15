#!/usr/bin/python3
import time
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['35.231.97.140', '35.237.159.72']
env.password = 'betty'


def do_clean(number=0):
    """keep number of version"""
    if number == '0':
        number = 1
    number = int(number) + 1
    with lcd("./versions/"):
        execute = local("ls -t | grep ^web_static_ | \
        tail -n +{} | xargs -r rm".format(number))
        if execute.failed:
            return False
    with cd("/data/web_static/releases/"):
        execute = run("ls -t | grep ^web_static | \
        tail -n +{} | xargs -r rm -rf".format(number))
        if execute.failed:
            return False
