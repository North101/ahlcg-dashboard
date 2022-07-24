import badger2040
from ahlcg2040.data import investigator_data
from badger_ui.base import App, Widget
from badger_ui.list import ListWidget
from badger_ui.util import Offset, Size

from .faction_tab import FactionTab
from .investigator_item import InvestigatorItemWidget
from .stats_screen import StatsScreen


class InvestigatorScreen(Widget):
  def __init__(self, parent: App, size: Size, offset: Offset = None):
    super().__init__(parent, size, offset)

    self.size = size
    self.page_item_count = 5
    self.faction_tab = FactionTab(
        parent=self,
        size=Size(self.size.width, 24),
        offset=Offset(0, 21 * 5)
    )
    self.create_list()

  def create_list(self):
    self.items = list(self.faction_items())
    self.list = ListWidget(
        parent=self,
        size=Size(self.size.width, self.size.height - 24),
        item_count=len(self.items),
        item_height=21,
        item_builder=self.item_builder,
        page_item_count=self.page_item_count,
    )

  def faction_items(self):
    for item in investigator_data.data:
      if item.faction == self.faction_tab.selected_index:
        yield item

  def item_builder(self, parent: ListWidget, index: int, selected: bool, size: Size, offset: Offset):
    return InvestigatorItemWidget(
        parent=parent,
        investigator=self.items[index],
        selected=selected,
        size=size,
        offset=offset,
    )

  def on_button(self, pressed: dict[int, bool]):
    if self.faction_tab.on_button(pressed):
      self.create_list()
      return True

    elif pressed[badger2040.BUTTON_B]:
      self.app.screen = StatsScreen(
          parent=self.app,
          size=self.app.size,
          investigator=self.items[self.list.selected_index],
      )
      return True

    return self.list.on_button(pressed) or super().on_button(pressed)

  def render(self):
    super().render()

    self.faction_tab.render()
    self.list.render()
