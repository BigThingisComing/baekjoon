arr = []

for i in range(9):
  arr.append(int(input()))

max_num = -1
max_index = -1

for i in range(9):
  if arr[i] > max_num:
    max_num = arr[i]
    max_index = i

print(max_num)
print(max_index+1)