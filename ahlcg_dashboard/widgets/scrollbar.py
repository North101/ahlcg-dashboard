from typing import TYPE_CHECKING

from ahlcg_dashboard.util import Offset, Size

if TYPE_CHECKING:
  from .base import Widget, SizedMixin
  from .list import ListWidget


class ScrollbarWidget(Widget[ListWidget], SizedMixin):
  def __init__(self, parent: ListWidget, width: int = 30):
    super().__init__(parent, Offset(parent.size.width - width, 0))

    self.size = Size(width, parent.size.height)

  @property
  def current(self):
    return self.parent.page_index

  @property
  def count(self):
    return self.parent.page_count

  def render(self):
    super().render()

    height = self.size.height
    segment_height = height // self.count
    segment_y_offset = segment_height * self.current

    # draw box
    self.display.pen(14)
    self.display.line(
        x=self.display_offset.x,
        y=self.display_offset.y,
        width=self.size.width,
        height=self.size.height,
    )

    # draw segment
    self.display.pen(15)
    self.display.rectangle(
        x=self.display_offset.x,
        y=self.display_offset.y + segment_y_offset,
        width=self.size.width,
        height=segment_height,
    )
