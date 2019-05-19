class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = []*capacity
  
  def append(self, item):
    self.storage.insert(self.current, item)
    self.storage.pop(self.current+1)
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
      return self.storage