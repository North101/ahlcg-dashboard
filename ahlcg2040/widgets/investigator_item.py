from ahlcg2040.data import Investigator
from badger_ui.base import Widget
from badger_ui.list import ListWidget
from badger_ui.util import Offset, Size


class InvestigatorItemWidget(Widget):
  parent: ListWidget

  def __init__(self, parent: ListWidget, investigator: Investigator, selected: bool, size: Size, offset: Offset = None):
    super().__init__(parent, size, offset)

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
