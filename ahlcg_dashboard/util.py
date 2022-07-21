from typing import NamedTuple


class Size(NamedTuple):
  width: int
  height: int


class Offset(NamedTuple):
  x: int
  y: int

  def __add__(self, other: 'Offset'):
    return Offset(self.x + other.x, self.y + other.y)

  def __sub__(self, other: 'Offset'):
    return Offset(self.x - other.x, self.y - other.y)
