import re
from itertools import product
   
def countVisited(mat):
  res = 0
  for line in mat:
    res += line.count("X")
  return res

# def walk(pos, mat, dir) -> list:
#   r, c = pos[0], pos[1]
#   mat[r][c] = 'X'
#   print(mat[r][c])
#   if r == 0 or r == len(mat)-1 or c == 0 or c == len(mat[0])-1:
#     print("out of bounds")
#     return mat
#   ud = dir.imag
#   rl = dir.real
#   print(r, c, ud, rl)
#   print( mat[int(r+ud)][int(c+rl)])
#   if mat[int(r+ud)][int(c+rl)] == "#":
#     dir = dirs[(dirs.index(dir)+1)%4]
#     return walk((int(r), int(c)), mat, dir)
#   return walk((int(r+ud), int(c+rl)), mat, dir)

def doWalk(pos, mat):
  # up and down changes the row
  dirs = [1+0j, 0+1j, -1+0j, 0-1j] # right, down, left, up
  dir = dirs[3]
  r, c = pos[0], pos[1]
  mat[r][c] = "X"
  while r > 0 and r < len(mat)-1 and c > 0 and c < len(mat[0])-1:
    ud = int(dir.imag)
    rl = int(dir.real)
    if mat[(r+ud)][(c+rl)] == "#":
      dir = dirs[(dirs.index(dir)+1)%4]
    else:
      r += ud
      c += rl
      mat[r][c] = "X"
  print(r, c, mat[r][c])
  return mat

def findStart(mat):
  for r in range(len(mat)):
    for c in range(len(mat[r])):
      if mat[r][c] == "^":
        return r, c

def main():
  with open("inp.txt", 'r') as file:
    lines = [list(x.strip()) for x in file.readlines()]
  print(type(lines[0][0]))
  r, c = findStart(lines)
  
  matAfterWalk = doWalk((r, c), lines)
  for line in matAfterWalk:
    print("".join(line))
  print(countVisited(matAfterWalk))


  
  
  


if __name__ == "__main__":
  main()
