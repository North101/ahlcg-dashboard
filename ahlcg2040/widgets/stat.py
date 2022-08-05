from ahlcg2040.data import number_icons, stat_icons
from badger_ui import App, Offset, Size, Widget


class StatWidget(Widget):
  def __init__(self, stat: int, value: int, selected: bool):
    self.value = value
    self.stat = stat
    self.selected = selected

  def render(self, app: App, size: Size, offset: Offset):
    number_icons.icon(
        display=app.display,
        icon_index=self.value,
        offset=offset,
    )
    stat_icons.icon(
        display=app.display,
        icon_index=self.stat,
        offset=offset + Offset(number_icons.size, 0),
    )
    if self.selected:
      height = offset.y + max(number_icons.size, stat_icons.size)
      app.display.line(
          offset.x,
          height,
          offset.x + number_icons.size + stat_icons.size,
          height,
      )
