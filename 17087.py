import sys

def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


N, S = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

for i in range(len(A)):
  A[i] = abs(S-A[i])

result = min(A)
for i in range(len(A)):
  result = gcd(A[i], result)

print(result)