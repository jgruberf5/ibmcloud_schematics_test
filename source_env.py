#!/usr/bin/env python3

import subprocess
import sys
import os
import json
import pip
import base64

from io import StringIO
from subprocess import Popen, PIPE

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
    #install_package('pyyaml')
    #import yaml
    # jsondata = json.loads(sys.stdin.read())
    env = os.environ
    for v in env.keys():
        jsondata[v] = env[v]
    file_index = 0
    for pathname in sys.path:
        jsondata['pythonpath_%d' % file_index] = pathname
        #file_index = file_index +1
        for root,dirs,files in os.walk(pathname):
            if 'ansible' not in root:
                jsondata["pythonpath_%d" % file_index] = root
                file_index = file_index + 1
    
    process = Popen(['/usr/bin/find', '/usr', '-name', 'openssl'], stdout=PIPE, stderr=subprocess.DEVNULL)
    (output, err) = process.communicate()
    exit_code = process.wait()

    jsondata['find_openssl_exit_code'] = exit_code
    jsondata["find_open_ssl_out"] = base64.b64encode(output).decode('utf-8')
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()