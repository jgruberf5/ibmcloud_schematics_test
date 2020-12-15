#!/usr/bin/env python3

import sys
import os
import json

def main():
    # jsondata = json.loads(sys.stdin.read())
    jsondata = {}
    env = os.environ
    for v in env.keys():
        jsondata[v] = env[v]
    modls = []
    for key in sys.modules.keys():
        modls.append(key)
    jsondata['installed_modules'] = modls
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()
