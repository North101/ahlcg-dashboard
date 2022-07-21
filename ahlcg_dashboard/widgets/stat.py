from typing import TYPE_CHECKING

from ahlcg_dashboard.util import Offset
from ahlcg_dashboard.data import stat_icons, number_icons

if TYPE_CHECKING:
  from .base import Widget, WidgetMixin


class StatWidget(Widget):
  def __init__(self, parent: WidgetMixin, offset: Offset, stat: int, value: int):
    super().__init__(parent, offset)

    self.value = value
    self.stat = stat

  def render(self):
    super().render()

    number_icons.icon(
      display=self.display,
      icon_index=self.value,
      offset=self.offset,
    )
    stat_icons.icon(
      display=self.display,
      icon_index=self.stat,
      offset=self.offset + Offset(number_icons.width, 0),
    )
