'''
https://www.hackerrank.com/challenges/30-conditional-statements?isFullScreen=true
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N%2!=0:
        print("Weird")
    elif N%2==0 and N in range(2,5):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    elif N>20:print("Not Weird")
    
    else:print("Not Weird")
