import icecream as ic
from collections import Counter


def parseInputAsLines():
  with open("inp.txt", 'r') as input:
    return input.readlines()

def main():
  lines = parseInputAsLines()
  l1 = []
  l2 = []
  for line in lines:
    one, two = line.split('   ')
    l1.append(int(one))
    l2.append(int(two))
  l1 = sorted(l1)
  l2 = sorted(l2)
  c = Counter(l2)
  ans = 0
  
  for i in range(len(l1)):
    ans += l1[i] * c[l1[i]]
  
  print(ans)


if __name__ == "__main__":
  main()
