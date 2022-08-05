import badger2040
from ahlcg2040.data import Investigator, Stats
from badger_ui import App, Offset, Size, Widget

from .stat import StatWidget


class StatsScreen(Widget):
  stat_offsets = [
      Offset(8, 38),
      Offset(80, 38),
      Offset(152, 38),
      Offset(224, 38),
      Offset(80, 84),
      Offset(152, 84),
  ]

  def __init__(self, investigator: Investigator):
    self.investigator = investigator
    self.selected_index = 0

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    from .investigator_screen import InvestigatorScreen

    if pressed[badger2040.BUTTON_A]:
      self.selected_index = (self.selected_index - 1) % len(self.investigator.stats)
      return True

    elif pressed[badger2040.BUTTON_B]:
      app.child = InvestigatorScreen()
      return True

    elif pressed[badger2040.BUTTON_C]:
      self.selected_index = (self.selected_index + 1) % len(self.investigator.stats)
      return True

    elif pressed[badger2040.BUTTON_UP]:
      self.investigator = Investigator(
          name=self.investigator.name,
          faction=self.investigator.faction,
          stats=Stats(*(
              value + 1 if i == self.selected_index else value
              for i, value in enumerate(self.investigator.stats)
          ))
      )
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      self.investigator = Investigator(
          name=self.investigator.name,
          faction=self.investigator.faction,
          stats=Stats(*(
              max(value - 1, 0) if i == self.selected_index else value
              for i, value in enumerate(self.investigator.stats)
          ))
      )
      return True

    return super().on_button(app, pressed)

  def render(self, app: App, size: Size, offset: Offset):
    app.display.pen(0)
    app.display.text(
        self.investigator.name,
        offset.x + ((size.width - app.display.measure_text(self.investigator.name, 0.8)) // 2),
        offset.y + (20 // 2),
        0.8,
    )
    for index, value in enumerate(self.investigator.stats):
      StatWidget(
          stat=index,
          selected=index == self.selected_index,
          value=value,
      ).render(app, size, offset + self.stat_offsets[index])
