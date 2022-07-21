from typing import TYPE_CHECKING, Optional

import badger2040
from ahlcg_dashboard.data import Investigator
from ahlcg_dashboard.util import Offset

from .base import Widget
from .stats_screen import StatsScreen

if TYPE_CHECKING:
  from .base import Widget
  from .list import ListWidget


class InvestigatorItemWidget(Widget[ListWidget]):
  def __init__(self, parent: ListWidget, investigator: Investigator, selected: bool, offset: Optional[Offset] = None):
    super().__init__(parent, offset)

    self.investigator = investigator
    self.selected = selected

  def on_button(self, button: int):
    if button == badger2040.BUTTON_B:
      self.app.screen = StatsScreen(
          parent=self.app,
          size=self.app.size,
          investigator=self.investigator
      )
      return True

    return False

  def render(self):
    self.display.pen(15 if self.selected else 0)
    self.display.rectangle(
        self.display_offset.x,
        self.display_offset.y,
        self.parent.size.width,
        self.parent.item_height,
    )
    self.display.pen(0 if self.selected else 15)

    self.display.font('bitmap6')
    self.display.text(
        text=self.investigator.name,
        x=self.display_offset.x,
        y=4,
    )
