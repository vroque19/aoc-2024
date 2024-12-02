from icecream import ic
import re
import sys
import math

def isSafe(nums):
  safe = True
  dir = 0
  if nums[0] - nums[1] < 0:
    dir = 1
  elif nums[0] - nums[1] > 0:
    dir = -1
  
  for i in range(1, len(nums)):
    curr_dir = 0
    diff = nums[i] - nums[i-1]
    if diff < 0:
      curr_dir = -1
    elif diff > 0:
      curr_dir = 1
    if abs(nums[i] - nums[i-1]) > 3:
      safe = False
    if curr_dir != dir:
      safe = False
    if curr_dir == 0 or dir == 0:
      safe = False
  return safe

def safeWithTolerance(nums):
  for i in range(len(nums)):
    curr_nums = nums[:i]+nums[i+1:]
    if isSafe(curr_nums):
      return True
  return False

def main():
  lines = parseInputAsLines()
  ans = 0
  for line in lines:
    nums = [int(x) for x in line.split(' ')]
    if isSafe(nums) or safeWithTolerance(nums):
      ans += 1
  print(ans)

def parseInputAsLines():
  with open("inp.txt", 'r') as input:
    return input.readlines()

if __name__ == "__main__":
  main()
