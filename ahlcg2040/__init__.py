from ahlcg2040.data import (faction_icons, investigator_data, number_icons,
                            stat_icons)
from ahlcg2040.widgets.app import MyApp

root_dir = '/'.join(__file__.rsplit('/')[:-1])
assets_dir = f'{root_dir}/assets'

def start():
  faction_icons.load()
  investigator_data.load()
  number_icons.load()
  stat_icons.load()

  app = MyApp()
  while True:
    app.update()
