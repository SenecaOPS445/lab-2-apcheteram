#!/usr/bin/env python3
# Author: Andy Persaud Cheteram
# Author ID: 148216229
# Date Created: 2025/01/20

import sys


if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')

