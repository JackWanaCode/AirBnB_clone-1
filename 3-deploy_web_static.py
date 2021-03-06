#!/usr/bin/python3
import time
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['35.231.97.140', '35.237.159.72']
env.password = 'betty'
path = None


def deploy():
    """compress web_static directory to .tgz"""
    global path
    if path is None:
        path = do_pack()
    if path is None:
        return False
    return do_deploy(path)


def do_deploy(archive_path):
    """compress web_static directory to .tgz"""
    if not os.path.isfile(archive_path):
        return False
    filename = archive_path.split("/")[-1]
    folder_name = filename.split(".")[0]
    del_file = "/tmp/{}".format(filename)
    deploy_folder = "/data/web_static/releases/{}".format(folder_name)
    upload = put(archive_path, "/tmp/{}".format(filename))
    if upload.failed:
        return False
    execute = run("mkdir -p {}".format(deploy_folder))
    if execute.failed:
        return False
    execute = run("tar -xzf {} -C {}".
                  format(del_file, deploy_folder))
    if execute.failed:
        return False
    execute = run("rm {}".format(del_file))
    if execute.failed:
        return False
    execute = run("mv {}/web_static/* {}/".format(deploy_folder,
                                                  deploy_folder))
    if execute.failed:
        return False
    execute = run("rm -rf {}/web_static".format(deploy_folder))
    if execute.failed:
        return False
    execute = run("rm -rf /data/web_static/current")
    if execute.failed:
        return False
    execute = run("ln -s {} /data/web_static/current".
                  format(deploy_folder))
    if execute.failed:
        return False
    print("New version deployed!")
    return True


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
