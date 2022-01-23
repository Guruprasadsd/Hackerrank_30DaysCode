'''
https://www.hackerrank.com/challenges/30-exceptions-string-to-integer?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys


try:
    print(int(input()))
except ValueError:
    print("Bad String")
