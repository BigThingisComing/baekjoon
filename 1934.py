import sys

tc_num = int(sys.stdin.readline())
for i in range(tc_num):
  A, B = map(int, sys.stdin.readline().split())
  a, b = A, B
  while b != 0:
    a = a % b
    a, b = b, a

  print((A*B)//a)
