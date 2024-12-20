import icecream as ic


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
  ans = 0
  for i in range(len(l1)):
    ans += abs(l1[i]-l2[i])
  
  with open("out1.txt", 'w') as f:
      print(ans, file=f)


if __name__ == "__main__":
  main()
