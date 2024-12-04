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
        print(dir, r, c)
        for kk in range(len(target)):
          print(mat[r+kk*dir[0]][c+kk*dir[1]], end='')
        print('<<')
  return res
        


def main():
  with open("inp.txt", 'r') as file:
    lines = [x.strip() for x in file.readlines()]
  cols = [[] for _ in range(len(lines[0]))]
  rows = lines
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      cols[j].append(lines[i][j])
  print(lines)


  values = [-1, 0, 1]
  dirs = list(product(values, repeat=2))
  print(dirs)
  res = 0
  xmas = "XMAS"
  # samx = "samx"
  for i in range(len(dirs)):
    res += getValid(lines, xmas, dirs[i])
    # res += getValid(lines, samx, dirs[i])
  print(res)

  
  
  


if __name__ == "__main__":
  main()
