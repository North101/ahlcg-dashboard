import badger2040
from ahlcg_dashboard.data import investigator_data
from ahlcg_dashboard.util import Offset, Size

from .base import App, SizedMixin, Widget
from .faction_tab import FactionTab
from .investigator_item import InvestigatorItemWidget
from .list import ListWidget
from .stats_screen import StatsScreen


class InvestigatorScreen(Widget, SizedMixin):
  def __init__(self, parent: App, size: Size, offset: Offset = None):
    super().__init__(parent, offset)

    self.size = size
    self.page_item_count = 5
    self.faction_tab = FactionTab(
        parent=self,
        size=Size(self.size.width, 24),
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
        offset=Offset(0, 24),
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

  def on_button(self, button: int):
    if self.faction_tab.on_button(button):
      self.create_list()
      return True

    elif button == self.buttons[badger2040.BUTTON_B]:
      self.app.screen = StatsScreen(
          parent=self.app,
          size=self.app.size,
          investigator=self.items[self.list.selected_index],
      )
      return True

    return self.list.on_button(button) or super().on_button(button)

  def render(self):
    super().render()

    self.faction_tab.render()
    self.list.render()
