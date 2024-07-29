# art.py

import sys
import random

chars = r"\|/"

def draw(rows,cols):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(cols)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py Nrows Ncolumns")
    draw(int(sys.argv[1]), int(sys.argv[2]))