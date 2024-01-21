import os

assert os.path.splitext('test.txt') == ('test', '.txt')
assert os.path.splitext('test') == ('test', '')
assert os.path.splitext('') == ('', '')
