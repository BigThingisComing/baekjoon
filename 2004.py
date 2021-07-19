"""
import operator as op
from functools import reduce

def nCr(n, r):
  if n < 1 or r < 0 or n < r:
    raise ValueError
  r = min(r, n-r)
  numerator = reduce(op.mul, range(n, n-r, -1), 1)
  denominator = reduce(op.mul, range(1, r+1), 1)
  return numerator // denominator

a, b = map(int, input().split())

nCr_result = nCr(a, b)

result = list(str(nCr_result))
result.reverse()

count = 0

for i in result:
  if i != '0':
    break
  count += 1

print(count)
"""

n, r = map(int, input().split())

def count_two(N):
  cnt = 0
  while N != 0:
    N = N // 2
    cnt += N
  return cnt

def count_five(N):
  cnt = 0
  while N != 0:
    N = N // 5
    cnt += N
  return cnt

print(min(count_two(n) - count_two(n - r) - count_two(r), count_five(n) - count_five(n - r) - count_five(r)))