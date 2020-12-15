#!/usr/bin/env python3

import sys
import os
import json
import pip

def install_package(package_name):
    pip.main(['install', package_name])

def main():
    install_package('wheel')
    install_package('pyyaml')
    # jsondata = json.loads(sys.stdin.read())
    jsondata = {}
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
