class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
  
  def append(self, item):
    self.storage.append(item)
    if len(self.storage) == self.capacity:
      self.current = 0
  
  def get(self):
      return self.storage