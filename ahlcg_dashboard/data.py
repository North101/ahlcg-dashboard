import struct
from enum import IntEnum
from typing import NamedTuple, Optional

from badger2040 import Badger2040

from ahlcg_dashboard.util import Offset


class Faction(IntEnum):
  Guardian = 0
  Seeker = 1
  Rogue = 2
  Mystic = 3
  Survivor = 4
  Neutral = 5


class Stats(NamedTuple):
  willpower: int
  intellect: int
  combat: int
  agility: int
  health: int
  sanity: int


class Investigator(NamedTuple):
  name: str
  faction: Faction
  stats: Stats


class InvestigatorData:
  fmt = struct.Struct('24sBBBBBBB')

  def __init__(self, data: Optional[list[Investigator]] = None):
    self.data = data

  def write(self):
    output = b''
    for item in self.data:
      output += self.fmt.pack(
          item.name.encode('ascii'),
          item.faction.value,
          item.stats.willpower,
          item.stats.intellect,
          item.stats.combat,
          item.stats.agility,
          item.stats.health,
          item.stats.sanity,
      )
    with open('assets/investigator.bin', 'wb') as f:
      f.write(output)

  def load(self):
    with open('assets/investigator.bin', 'rb') as f:
      data = self.fmt.iter_unpack(f.read())

    self.data = [
        Investigator(
            name=name.decode('ascii'),
            faction=Faction[faction],
            stats=Stats(*stats),
        )
        for (name, faction, *stats) in data
    ]


investigator_data = InvestigatorData()


class IconSheet:
  def __init__(self, path: str, width: int, height: int, count: int):
    self.path = path
    self.width = width
    self.height = height
    self.count = count
    self.data = bytearray(self.sheet_width * self.height // 8)

  @property
  def sheet_width(self):
    return self.width * self.count

  def load(self):
    with open(self.path, 'r') as f:
      f.readinto(self.data)

  def icon(self, display: Badger2040, icon_index: int, offset: Offset):
    display.icon(
        data=self.data,
        icon_index=icon_index,
        sheet_size=self.sheet_width,
        icon_size=self.width,
        dx=offset.x,
        dy=offset.y,
    )


class NumberIconSheet(IconSheet):
  def __init__(self):
    super().__init__('assets/number_icons.bin', 32, 32, 10)


class StatIconSheet(IconSheet):
  def __init__(self):
    super().__init__('assets/stat_icons.bin', 32, 32, 6)


class FactionIconSheet(IconSheet):
  def __init__(self):
    super().__init__('assets/faction_icons.bin', 32, 32, 6)


number_icons = NumberIconSheet()
stat_icons = StatIconSheet()
faction_icons = FactionIconSheet()
