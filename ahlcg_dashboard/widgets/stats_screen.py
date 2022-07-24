import badger2040
from ahlcg_dashboard.data import Investigator, Stats
from ahlcg_dashboard.util import Offset, Size

from .base import SizedMixin, Widget, WidgetMixin
from .stat import StatWidget


class StatsScreen(Widget, SizedMixin):
  stat_offsets = [
      Offset(8, 38),
      Offset(80, 38),
      Offset(152, 38),
      Offset(224, 38),
      Offset(80, 84),
      Offset(152, 84),
  ]

  def __init__(self, parent: WidgetMixin, size: Size, investigator: Investigator, offset: Offset = None):
    super().__init__(parent, offset)

    self.size = size
    self.investigator = investigator
    self.selected_index = 0

  def on_button(self, pressed: dict[int, bool]) -> bool:
    from .investigator_screen import InvestigatorScreen

    if pressed[badger2040.BUTTON_A]:
      self.selected_index = (self.selected_index - 1) % len(self.investigator.stats)
      return True

    elif pressed[badger2040.BUTTON_B]:
      self.app.screen = InvestigatorScreen(
          parent=self.app,
          size=self.app.size,
      )
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

    return super().on_button(pressed)

  def render(self):
    self.display.pen(0)
    self.display.text(
        self.investigator.name,
        self.display_offset.x + ((self.size.width - self.display.measure_text(self.investigator.name, 0.8)) // 2),
        self.display_offset.y + (20 // 2),
        0.8,
    )
    for index, value in enumerate(self.investigator.stats):
      StatWidget(
          parent=self,
          offset=self.stat_offsets[index],
          stat=index,
          selected=index == self.selected_index,
          value=value,
      ).render()
