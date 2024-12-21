import os

# Using readlines()
from pathlib import Path

file1 = os.path.join('F:\\', 'extras\\', 'testing out.txt')
file2 = open(file1)
contents = file2.read()

print(contents)