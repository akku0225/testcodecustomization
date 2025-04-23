"""
Author: Abhishek
Date Updated: 3 Oct 2022
"""

from heapq import *
from collections import Counter

s1 = "Hello Huffman"

def huffman_coding(s):
    f = Counter(s)

    heap1 = [[f, [char, ""]] for f, char in f.items()]
    heapify(heap1)

    while len(heap1) > 1:
        right = heappop(heap1) # 0
        left = heappop(heap1) # 1

        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]

        heappush(heap1, ([right[0] + left[0]] + right[1:] + left[1:]))

    return heap1
