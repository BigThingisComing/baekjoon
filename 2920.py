arr = list(map(int, input().split()))

if arr[0] == 1:
  for i in range(8):
    if arr[i] != i+1:
      print("mixed")
      break
  if i == 7:
    print("ascending")
elif arr[0] == 8:
  for i in range(8):
    if arr[i] != 8-i:
      print("mixed")
      break
  if i == 7:
    print("descending")
else:
  print("mixed")