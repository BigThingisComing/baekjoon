N, B = input().split()
B = int(B)

result = 0

for i, j in enumerate(N):
  if ord(j) >= 65:
    result += (ord(j) - 65 + 10) * B ** (len(N) - i - 1)
  else:
    result += int(j) * B ** (len(N) - i - 1)

print(result)