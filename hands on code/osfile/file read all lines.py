import os

# Using readlines()
file1 = open('F:\\SOFTWARES.txt')
Lines = file1.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))