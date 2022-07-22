import badger2040

from ahlcg_dashboard.data import investigator_data, stat_icons, number_icons
from ahlcg_dashboard.widgets.app import MyApp


def main():
  number_icons.load()
  stat_icons.load()
  investigator_data.load()

  display = badger2040.Badger2040()
  display.update_speed(badger2040.UPDATE_FAST)

  app = MyApp(display=display)
  while True:
    app.update()


if __name__ == '__main__':
  main()
