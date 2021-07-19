import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

prime_num = 0

for num in arr:
  torf = True
  if num == 1:
    torf = False
  for i in range(2, num):
    if num % i == 0:
      torf = False
      break
  if torf:
    prime_num += 1

print(prime_num)