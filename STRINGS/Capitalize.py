#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitaliz())
    return s

