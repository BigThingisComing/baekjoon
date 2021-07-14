import sys
input = sys.stdin.readline

class Stack:
  def __init__(self):
    self.st = []
    self.len = 0
  
  def push(self, num):
    self.st.append(num)
    self.len += 1
  
  def pop(self):
    if self.len > 0:
      tmp = self.st[self.len-1]
      self.st.pop()
      self.len -= 1
      return tmp
    else:
      return -1
  
  def size(self):
    return self.len
  
  def empty(self):
    if self.len == 0:
      return 1
    else:
      return 0
  
  def top(self):
    if self.len == 0:
      return -1
    else:
      return self.st[self.len-1]

com_num = int(input())

stk = Stack()

for i in range(com_num):
  Command = input().split()
  if Command[0] == 'push':
    stk.push(Command[1])
  elif Command[0] == 'pop':
    print(stk.pop())
  elif Command[0] == 'size':
    print(stk.size())
  elif Command[0] == 'empty':
    print(stk.empty())
  elif Command[0] == 'top':
    print(stk.top())