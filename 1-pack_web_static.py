#!/usr/bin/python3
import time
from fabric.api import *


def do_pack():
    """compress web_static directory to .tgz"""
    execute = local("mkdir -p versions")
    timestr = time.strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(timestr)
    execute = local("tar -cvzf versions/{} web_static".format(filename))
    if execute.failed:
        return None
    else:
        return "versions/{}".format(filename)
