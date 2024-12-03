import re

# modify the input using regex and deleting the last don't()...
def main():
  with open("inp.txt", 'r') as file:
    input = file.readlines()
  group1 = "mul(\(\d+,\d+\))"
  valid = re.findall(group1, str(input))
  ans = 0
  for pair in valid:
    pair = pair.strip("()")
    dig1, dig2 = pair.split(',')
    ans += int(dig1) * int(dig2)

  print(ans)


if __name__ == "__main__":
  main()
