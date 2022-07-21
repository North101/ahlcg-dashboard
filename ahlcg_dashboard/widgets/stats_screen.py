from typing import TYPE_CHECKING, Optional

from ahlcg_dashboard.data import Investigator
from ahlcg_dashboard.util import Offset, Size

from .stat import StatWidget

if TYPE_CHECKING:
  from .base import Widget, WidgetMixin, SizedMixin


class StatsScreen(Widget, SizedMixin):
  stat_offsets = [
      Offset(8, 38),
      Offset(80, 38),
      Offset(152, 38),
      Offset(224, 38),
      Offset(80, 84),
      Offset(152, 84),
  ]

  def __init__(self, parent: WidgetMixin, size: Size, investigator: Investigator, offset: Optional[Offset] = None):
    super().__init__(parent, offset)

    self.size = size
    self.investigator = investigator
    self.stats = [
        StatWidget(
            parent=self,
            offset=self.stat_offsets[index],
            stat=index,
            value=value,
        )
        for index, value in enumerate(investigator.stats)
    ]

  def render(self):
    self.display.pen(15)
    self.display.font('bitmap6')
    self.display.text(
        text=self.investigator.name,
        x=(self.size.width - self.display.measure_text(self.investigator.name)) // 2,
        y=4,
    )
    for stat in self.stats:
      stat.render()
