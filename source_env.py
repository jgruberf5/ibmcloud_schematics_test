#!/usr/bin/env python3

import sys
import os
import json
import pip

from io import StringIO

INSTALL_DIR = '/tmp/pythonlib'

def install_package(package_name):
    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)
    if INSTALL_DIR not in sys.path:
        sys.path.append(INSTALL_DIR)
    origin_stdout = sys.__stdout__
    pip_out = StringIO()
    sys.stdout = pip_out
    pip.main(['install', "--target=%s" % INSTALL_DIR, package_name])
    sys.stdout = origin_stdout
    return pip_out.readlines()

def main():
    jsondata = {}
    install_package('pyyaml')
    import yaml
    # jsondata = json.loads(sys.stdin.read())
    env = os.environ
    for v in env.keys():
        jsondata[v] = env[v]
    for pathname in sys.path:
        file_index = 0
        jsondata['pythonpath_%d' % file_index] = pathname
        file_index = file_index +1
        #for root,dirs,files in os.walk(pathname):
        #    if 'ansible' not in root:
        #        jsondata["pythonpath_%d" % file_index] = root
        #        file_index = file_index + 1
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()