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
    for key in sys.modules.keys():
        jsondata[key] = 'installed'
    sys.stdout.write(json.dumps(jsondata))

if __name__ == '__main__':
    main()
