import sys
input = sys.stdin.readline

class Deque:
  def __init__(self):
    self.d = []
    self.len = 0
  
  def push_front(self, num):
    self.d.insert(0,num)
    self.len += 1

  def push_back(self, num):
    self.d.append(num)
    self.len += 1
  
  def pop_front(self):
    if self.len > 0:
      self.len -= 1
      tmp = self.d[0]
      self.d = self.d[1:]
      return tmp
    else:
      return -1

  def pop_back(self):
    if self.len > 0:
      self.len -= 1
      tmp = self.d.pop()
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
  
  def front(self):
    if self.len == 0:
      return -1
    else:
      return self.d[0]

  def back(self):
    if self.len == 0:
      return -1
    else:
      return self.d[self.len-1]

com_num = int(input())

deque = Deque()

for i in range(com_num):
  Command = input().split()
  if Command[0] == 'push_front':
    deque.push_front(Command[1])
  elif Command[0] == 'push_back':
    deque.push_back(Command[1])
  elif Command[0] == 'pop_front':
    print(deque.pop_front())
  elif Command[0] == 'pop_back':
    print(deque.pop_back())
  elif Command[0] == 'size':
    print(deque.size())
  elif Command[0] == 'empty':
    print(deque.empty())
  elif Command[0] == 'front':
    print(deque.front())
  elif Command[0] == 'back':
    print(deque.back())