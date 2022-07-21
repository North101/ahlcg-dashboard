from typing import TYPE_CHECKING, Optional

from ahlcg_dashboard.util import Offset, Size

if TYPE_CHECKING:
  from .base import Widget, WidgetMixin, SizedMixin


class ImageWidget(Widget, SizedMixin):
  def __init__(self, parent: WidgetMixin, size: Size, path: str, offset: Optional[Offset] = None):
    super().__init__(parent, offset)

    self.size = size
    self.path = path
    self.image = bytearray(int(size.width * size.height / 8))
    with open(path, "r") as f:
      f.readinto(self.image)

  def render(self):
    self.display.image(
        self.image,
        width=self.size.width,
        height=self.size.height,
        x=self.display_offset.x,
        y=self.display_offset.y,
    )
