#!/usr/bin/env python3

import sys
import os
import json
import pip

from io import StringIO

def install_package(package_name):
    origin_stdout = sys.__stdout__
    pip_out = StringIO()
    sys.stdout = pip_out
    pip.main(['install', package_name, '--user'])
    sys.stdout = origin_stdout
    return pip_out.readlines()

def main():
    jsondata = {}
    std_out = install_package('pyyaml')
    jsondata['installpyyaml'] = '|'.join(std_out)
    # jsondata = json.loads(sys.stdin.read())
    env = os.environ
    for v in env.keys():
        jsondata[v] = env[v]
    for pathname in sys.path:
        file_index = 0
        for root,dirs,files in os.walk(pathname):
            if 'ansible' not in root:
                jsondata["pythonpath_%d" % file_index] = root
                file_index = file_index + 1
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()