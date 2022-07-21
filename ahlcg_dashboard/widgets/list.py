from typing import TYPE_CHECKING, Optional, Protocol

import badger2040
from ahlcg_dashboard.util import Offset, Size

from .scrollbar import ScrollbarWidget

if TYPE_CHECKING:
  from .base import SizedMixin, Widget, WidgetMixin


class ListItemBuilder(Protocol):
  def __call__(self, parent: 'ListWidget', index: int, selected: bool) -> WidgetMixin:
    pass


class ListWidget(Widget, SizedMixin):
  _selected_index = 0
  children: list[WidgetMixin] = None

  def __init__(
      self,
      parent: WidgetMixin,
      size: Size,
      item_height: int,
      item_count: int,
      item_builder: ListItemBuilder,
      page_item_count: int,
      selected_index: int = 0,
      offset: Optional[Offset] = None,
  ):
    super().__init__(parent, offset)

    self.size = size
    self.item_count = item_count
    self.item_height = item_height
    self.item_builder = item_builder
    self.selected_index = selected_index
    self.page_item_count = page_item_count
    self.scrollbar = ScrollbarWidget(parent=self)
    self.children = [
        self.item_builder(
            parent=self,
            index=i,
            selected=i == self.selected_child_index,
        )
        for i in range(self.page_start, self.page_stop)
    ]

  @property
  def page_index(self):
    return self.selected_index // self.page_item_count

  @property
  def page_count(self):
    return ((self.item_count - 1) // self.page_item_count) + 1

  @property
  def page_start(self):
    return self.page_index * self.page_item_count

  @property
  def page_stop(self):
    return self.page_start + self.page_item_count

  @property
  def selected_child_index(self):
    return self.selected_index % self.page_item_count

  @property
  def selected_child(self):
    return self.children[self.selected_child_index]

  def on_button(self, button: int):
    if button == badger2040.BUTTON_UP:
      self.selected_index = max(self.selected_index - 1, 0)
      return True
    elif button == badger2040.BUTTON_DOWN:
      self.selected_index = min(self.selected_index + 1, self.item_count)
      return True

    return self.selected_child.on_button(button)

  def render(self):
    super().render()

    for child in self.children:
      child.render()
    self.scrollbar.render()
