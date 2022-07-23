import badger2040

from ahlcg_dashboard.data import (faction_icons, investigator_data,
                                  number_icons, stat_icons)
from ahlcg_dashboard.widgets.app import MyApp


def main():
  faction_icons.load()
  investigator_data.load()
  number_icons.load()
  stat_icons.load()

  display = badger2040.Badger2040()
  display.update_speed(badger2040.UPDATE_FAST)

  app = MyApp(display=display)
  while True:
    app.update()


main()
