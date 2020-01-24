from typing import List, Iterable, Dict
from math import log2
import copy

from invertedindex import InvertedIndex, Document

# tests
if __name__ == "__main__":
    print("-- Test 1 ---\nDoc1: this is test number one\nDoc2: this is test number two")
    documents  = [Document("Doc1", ["this", "is", "test", "number", "one"]), Document("Doc2", ["this", "is", "test", "number", "two"])]
    index = InvertedIndex(documents)
    print(f'Testing with query: number one. Rankings: {index.retrieve(["number", "one"])}')
    print(f'Testing with query: number two. Rankings: {index.retrieve(["number", "two"])}')
