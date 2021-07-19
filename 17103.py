import sys

r = 1000000

check = [True for _ in range(r)]

for i in range(2, int(r**0.6)):
  if check[i] == True:
    for j in range(i*2, r, i):
      if check[j] == True:
        check[j] = False


tc_num = int(sys.stdin.readline())
cnt = 0

for _ in range(tc_num):
  n = int(sys.stdin.readline())
  cnt = 0
  for i in range(3, n // 2 + 1, 2):
    if check[i] == True:
      if check[n-i] == True:
        cnt += 1
  print(cnt)
