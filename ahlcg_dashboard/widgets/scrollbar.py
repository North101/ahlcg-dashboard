from ahlcg_dashboard.util import Offset, Size

from .base import SizedMixin, Widget


class ScrollbarWidget(Widget, SizedMixin):
  def __init__(self, parent: 'ListWidget', size: Size, offset: Offset = None):
    super().__init__(parent, offset)

    self.size = size

  @property
  def current(self):
    return self.parent.page_index

  @property
  def count(self):
    return self.parent.page_count

  def render(self):
    super().render()

    height = self.size.height

    # draw box
    start_x = self.display_offset.x
    start_y = self.display_offset.y
    stop_x = self.display_offset.x + self.size.width - 1
    stop_y = self.display_offset.y + height
    self.display.pen(0)
    # top
    self.display.line(
        start_x,
        start_y,
        stop_x,
        start_y,
    )
    # left
    self.display.line(
        start_x,
        start_y,
        start_x,
        stop_y,
    )
    self.display.line(
        start_x,
        stop_y,
        stop_x,
        stop_y,
    )
    self.display.line(
        stop_x,
        start_y,
        stop_x,
        stop_y,
    )

    # draw segment
    segment_height = height // self.count
    segment_y_offset = segment_height * self.current
    self.display.rectangle(
        self.display_offset.x,
        self.display_offset.y + segment_y_offset,
        self.size.width,
        segment_height,
    )
