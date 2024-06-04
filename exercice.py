#les modules
def addition(a, b):
    return a + b

if __name__ == "__main__":
    print(addition(4, 5)) 

import sys

from pprint import pprint
pprint(sys.path)

#les anotations
def add(a: int, b: int) -> int:
    return a + b

add(1, 3)