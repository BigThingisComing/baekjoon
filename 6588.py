"""
def isPrime(num):
  a = []
  if num == 1:
    return False
  else:
    for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
        return False
    return True

prime_num = []

for i in range(3, 500000):
  if isPrime(i):
    prime_num.append(i)

while True:
  num = int(input())
  
  if num == 0:
    break

  flag = False
  
  for i in prime_num[::-1]:
    if flag == True:
      break
    for j in range(len(prime_num)):
      if num == (i + prime_num[j]):
        print("{} = {} + {}".format(num, prime_num[j], i))
        flag == True
    
  if flag == False:
    print("Goldbach's conjecture is wrong.")
"""
r= 1000000

check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i) : 
            if check[j] == True :
                check[j] = False

import sys
input = sys.stdin.readline


while(True):
    n = int(input())

    if n==0 : break
    for i in range(3,r):
        if check[i] == True:
            if check[n-i] == True :
                print("%d = %d + %d"%(n , i , n-i))
                break