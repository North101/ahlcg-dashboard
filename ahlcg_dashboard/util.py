from collections import namedtuple

Size = namedtuple('Size', [
    'width',
    'height',
])


class Offset:
  x: int
  y: int

  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __add__(self, other: 'Offset'):
    return Offset(self.x + other.x, self.y + other.y)

  def __sub__(self, other: 'Offset'):
    return Offset(self.x - other.x, self.y - other.y)

  def __repr__(self):
    return f'Offset(x={self.x}, y={self.y})'


class BoundInt:
  def __init__(self, value: int, start: int, stop: int):
    self.value = value
    self.start = start
    self.stop = stop

  def bound(self, value: int):
    if self.start:
      value = max(value, self.start)
    if self.stop:
      value = min(value, self.stop)
    return value

  def __add__(self, other):
    self.value = self.bound(self.value + other)

  def __sub__(self, other):
    self.value = self.bound(self.value - other)

  def __eq__(self, other):
    return self.value == other


class WrapInt:
  def __init__(self, value: int, max: int):
    self.value = value
    self.max = max

  def wrap(self, value: int):
    return value % self.max

  def __add__(self, other):
    self.value = self.wrap(self.value + other)

  def __sub__(self, other):
    self.value = self.wrap(self.value - other)

  def __eq__(self, other):
    return self.value == other
