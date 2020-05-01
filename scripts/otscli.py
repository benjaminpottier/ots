#!/usr/bin/python3

import os
import sys
import fire
from ots import Ots

path = os.path.expanduser('~/.ots')

if not os.path.exists(path):
    print(f"Please create {path} with username:api_key.")
    sys.exit(1)

with open(path) as f:
    user, api_key = f.read().rstrip().split(':')

if __name__ == '__main__':
  fire.Fire(Ots(user, api_key))
  
