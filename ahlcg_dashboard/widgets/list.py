import badger2040
from ahlcg_dashboard.util import Offset, Size

from .base import SizedMixin, Widget, WidgetMixin
from .scrollbar import ScrollbarWidget


class ListItemBuilder:
  def __call__(self, parent: 'ListWidget', index: int, selected: bool, size: Size, offset: Offset) -> WidgetMixin:
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
      offset: Offset = None,
  ):
    super().__init__(parent, offset)

    self.size = size
    self.item_count = item_count
    self.item_height = item_height
    self.item_builder = item_builder
    self.selected_index = selected_index
    self.page_item_count = page_item_count
    self.scrollbar = ScrollbarWidget(
        parent=self,
        size=Size(6, self.size.height),
        offset=Offset(self.size.width - 6, 0),
    )

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
    i = self.selected_child_index
    return self.item_builder(
        parent=self,
        index=i,
        selected=True,
        size=Size(self.size.width - self.scrollbar.size.width, self.item_height),
        offset=Offset(0, self.item_height * (i % self.page_item_count)),
    )

  def on_button(self, button: int):
    if button == self.buttons[badger2040.BUTTON_UP]:
      self.selected_index = (self.selected_index - 1) % self.item_count
      return True
    elif button == self.buttons[badger2040.BUTTON_DOWN]:
      self.selected_index = (self.selected_index + 1) % self.item_count
      return True

    return super().on_button(button)

  def render(self):
    super().render()

    for i in range(self.page_start, min(self.page_stop, self.item_count)):
      child = self.item_builder(
          parent=self,
          index=i,
          selected=(i == self.selected_index),
          size=Size(self.size.width - self.scrollbar.size.width, self.item_height),
          offset=Offset(0, self.item_height * (i % self.page_item_count)),
      )
      child.render()
    self.scrollbar.render()
