import sys
import re

count = 0
for line in sys.stdin:
    for win in line.split():
        if re.search("^[0-9]+$", win):
            count += 1
print(count)