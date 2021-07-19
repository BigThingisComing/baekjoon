def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

tc_num = int(input())

for _ in range(tc_num):
  num = list(map(int, input().split()))
  sum = 0
  for i in range(num[0]):
    for j in range(num[0]):
      if i < j:
        sum += gcd(num[i+1], num[j+1])
  
  print(sum)