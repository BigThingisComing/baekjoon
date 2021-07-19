num_len = int(input())
num_str = input()
num_arr = list(num_str)

sum = 0
for i in range(len(num_arr)):
  sum += int(num_arr[i])

print(sum)