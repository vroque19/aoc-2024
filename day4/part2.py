import re
from itertools import product


def getValid(mat, target, dir):
  res = 0
  for r in range(len(mat)):
    for c in range(len(mat[r])):
      good = True
      for i in range(len(target)):
        curr_r = r+i*dir[0]
        curr_c = c+i*dir[1]
        if curr_r < 0 or curr_r > len(mat[0]) or curr_c < 0 or curr_c > len(mat):
          good = False
          break
        try:
            if mat[curr_r][curr_c] == target[i]:
                continue
            else:
                good = False
            break
        except:
          good = False
          break
      res += 1 if good else 0
      if good:
        # print(good, dir, r, c)
        # for kk in range(len(target)):
        #   print(mat[r+kk*dir[0]][c+kk*dir[1]], end='')
        # print('<<')
        return good
        print("good is: ", good)
      
  # print(f"good:{good}")
  return good
        


def main():
  with open("inp.txt", 'r') as file:
    lines = [x.strip() for x in file.readlines()]
  cols = [[] for _ in range(len(lines[0]))]
  


  values = [-1, 1]
  dirs = list(product(values, repeat=2))
  print(dirs)
  res = 0
  mas = "MAS"
  sam = "SAM"
  val = False
  for k in range(len(lines)-2):
    for j in range(len(lines[0])-2):
      small_lines = [row[j:j+3] for row in lines[k:k+3]]
      # print(small_lines)
      out = []
      for i in range(len(dirs)):
        out.append(getValid(small_lines, mas, dirs[i]))
        # print("val:", val)
      res += 1 if out.count(True)==2 else 0
      print(out.count(True))
  print(res)

  


if __name__ == "__main__":
  main()
