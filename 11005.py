string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = list(map(int, input().split()))
answer = []

while N != 0:
  answer.insert(0, str(string[N % B]))
  N //= B

print(''.join(answer))