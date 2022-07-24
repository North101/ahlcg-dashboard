from ahlcg2040.data import number_icons, stat_icons
from badger_ui.base import Widget, WidgetMixin
from badger_ui.util import Offset, Size


class StatWidget(Widget):
  def __init__(self, parent: WidgetMixin, size: Size, stat: int, value: int, selected: bool, offset: Offset = None):
    super().__init__(parent, size, offset)

    self.value = value
    self.stat = stat
    self.selected = selected

  def render(self):
    super().render()

    number_icons.icon(
        display=self.display,
        icon_index=self.value,
        offset=self.display_offset,
    )
    stat_icons.icon(
        display=self.display,
        icon_index=self.stat,
        offset=self.display_offset + Offset(number_icons.size, 0),
    )
    if self.selected:
      height = self.display_offset.y + max(number_icons.size, stat_icons.size)
      self.display.line(
          self.display_offset.x,
          height,
          self.display_offset.x + number_icons.size + stat_icons.size,
          height,
      )
