#!/usr/bin/env python3

import sys
import os
import json
import subprocess

def install_package(package_name):
    proc = subprocess.Popen(['pip', 'install', package_name], stdout=subprocess.PIPE)
    return proc.stdout

def main():
    jsondata = {}
    std_out = install_package('wheel')
    jsondata['installwheelout'] = std_out.read().replace('\n','|')
    std_out = install_package('pyyaml')
    jsondata['installpyyaml'] = std_out.read().replace('\n','|')
    # jsondata = json.loads(sys.stdin.read())
    env = os.environ
    for v in env.keys():
        jsondata[v] = env[v]
    #for pathname in sys.path:
    #    file_index = 0
    #    for root,dirs,files in os.walk(pathname):
    #        if 'ansible' not in root:
    #            jsondata["pythonpath_%d" % file_index] = root
    #            file_index = file_index + 1
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()