tc = int(input())
out_arr = []

for i in range(tc):
  num, s = input().split()
  tmp = ''

  for j in range(len(s)):
    for k in range(int(num)):
      tmp += s[j]
    
  out_arr.append(tmp)

for i in range(tc):
  print(out_arr[i])