def factorial(N):
  if N == 0 or N == 1:
    return 1
  else:
    return N*factorial(N-1)

num = int(input())
numtostr = list(str(factorial(num)))
numtostr.reverse()

count = 0

for i in numtostr:
  if i != '0':
    break
  count += 1

print(count)