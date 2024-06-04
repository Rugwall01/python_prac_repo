# Below I am taking a slice by specifying the start and end of the part of the list I want after the list. In this cas argv is the list, look below

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


# See how after sys.argv here I put [1:] this starts the list at index 1 instead of 0 and then goes until the end. It goes until the end because I left the second constraint (space after the colon in the brackets) completely blank. If I had specified another index value it would print the indexes in-between each index value and include each index value itself


# You can use negative numbers in the argv range inside [] such as [1:-1], in this case the [0] index is excluded as well as whatever the last argument is by the [ :-1] part of this 


















