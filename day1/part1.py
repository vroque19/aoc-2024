import icecream as ic


def parseInputAsLines():
  with open("inp.txt", 'r') as input:
    return input.readlines()

def main():
  lines = parseInputAsLines()
  ans = 0
  with open("out.txt", 'w') as f:
    print(ans, file=f)


if __name__ == "__main__":
  main()
