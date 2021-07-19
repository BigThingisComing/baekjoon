A, B = list(map(int, input().split()))
length = int(input())
A_num = list(map(int, input().split()))

A_result = 0

for i in range(length):
  A_result += A_num[i] * A ** (length - i - 1)

answer = []

while A_result != 0:
  answer.insert(0, A_result % B)
  A_result //= B

print(' '.join(map(str, answer)))