N = int(input())

prime_num = 2

while N > 1:
  if (N % prime_num) == 0:
    print(prime_num)
    N //= prime_num
  else:
    prime_num += 1