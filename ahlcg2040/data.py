import struct
from collections import namedtuple

from badger_ui.util import IconSheet


class Faction:
  values = [
      'Guardian',
      'Seeker',
      'Rogue',
      'Mystic',
      'Survivor',
      'Neutral',
  ]

  def __len__(self):
    return len(self.values)

  def __getitem__(self, key: str):
    return self.values.index(key)

  def __call__(self, value):
    return value


Stats = namedtuple('Stats', [
    'willpower',
    'intellect',
    'combat',
    'agility',
    'health',
    'sanity',
])


Investigator = namedtuple('Investigator', [
    'name',
    'faction',
    'stats',
])


class InvestigatorData:
  fmt = '24sBBBBBBB'

  def __init__(self, data=None):
    self.path = 'ahlcg2040/assets/investigator.bin'
    self.data = data

  def write(self):
    output = b''
    for item in self.data:
      output += struct.pack(
          self.fmt,
          item.name.encode('ascii'),
          item.faction,
          item.stats.willpower,
          item.stats.intellect,
          item.stats.combat,
          item.stats.agility,
          item.stats.health,
          item.stats.sanity,
      )
    with open(self.path, 'wb') as f:
      f.write(output)

  def load(self):
    size = struct.calcsize(self.fmt)
    offset = 0
    with open(self.path, 'rb') as f:
      a = b''
      while True:
        b = f.read()
        if not b:
          break
        a += b
      data = []
      while offset < len(a):
        data.append(struct.unpack_from(self.fmt, a, offset))
        offset += size

    self.data = [
        Investigator(
            name=name.decode('ascii'),
            faction=faction,
            stats=Stats(*stats),
        )
        for (name, faction, *stats) in data
    ]


investigator_data = InvestigatorData()


class NumberIconSheet(IconSheet):
  def __init__(self):
    super().__init__('ahlcg2040/assets/number_icons.bin', 32, 10)


class StatIconSheet(IconSheet):
  def __init__(self):
    super().__init__('ahlcg2040/assets/stat_icons.bin', 32, 6)


class FactionIconSheet(IconSheet):
  def __init__(self):
    super().__init__('ahlcg2040/assets/faction_icons.bin', 24, 6 * 2)


number_icons = NumberIconSheet()
stat_icons = StatIconSheet()
faction_icons = FactionIconSheet()
