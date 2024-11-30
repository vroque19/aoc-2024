import icecream as ic
import re
import sys


def main():
  lines = parseInputAsLines()
  ans = 0
  with open('out1.txt', 'w') as f:
    print(ans, file=f) 

def parseInputAsLines():
  with open("inp.txt", 'r') as input:
    return input.readlines()

if __name__ == "__main__":
  main()
