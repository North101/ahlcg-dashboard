import badger2040
from ahlcg_dashboard.data import Investigator
from ahlcg_dashboard.util import Offset, Size

from .base import SizedMixin, Widget
from .list import ListWidget


class InvestigatorItemWidget(Widget, SizedMixin):
  parent: ListWidget

  def __init__(self, parent: ListWidget, investigator: Investigator, selected: bool, size: Size, offset: Offset = None):
    super().__init__(parent, offset)

    self.size = size
    self.investigator = investigator
    self.selected = selected

  def render(self):
    self.display.pen(0)
    if self.selected:
      self.display.rectangle(
          self.display_offset.x,
          self.display_offset.y,
          self.size.width,
          self.size.height
      )
      self.display.pen(15)
    self.display.thickness(2)
    self.display.text(
        self.investigator.name,
        self.display_offset.x + 2,
        self.display_offset.y + (self.size.height // 2),
        0.8,
    )
