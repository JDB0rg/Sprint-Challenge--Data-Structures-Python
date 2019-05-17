class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]#*capacity

  class __Full:
    def append(self, item):
      self.storage[self.current] = item
      self.current = (self.current + 1) % self.capacity

    def get(self):
      return self.storage[self.current:] + self.data[:self.current]
  
  def append(self, item):
    self.storage.append(item)
    if len(self.storage) == self.capacity:
      self.current = 0
      self.__class__ = self.__Full
  
  def get(self):
      return self.storage