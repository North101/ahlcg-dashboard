from typing import TYPE_CHECKING

import badger2040
from ahlcg_dashboard.data import Faction, investigator_data
from ahlcg_dashboard.util import Offset, Size

from .investigator_item import InvestigatorItemWidget
from .list import ListWidget

if TYPE_CHECKING:
  from .base import SizedMixin, Widget, WidgetMixin


class InvestigatorScreen(Widget, SizedMixin):
  def __init__(self, parent: WidgetMixin, size: Size, offset: Offset):
    super().__init__(parent, offset)

    self.size = size
    self.items = investigator_data
    self.faction = Faction.Guardian
    self.page_item_count = 7

  @property
  def faction(self):
    return self._faction

  @faction.setter
  def faction(self, value: Faction):
    self._faction = value
    self.create_list()

  def faction_items(self):
    for item in self.items:
      if item.faction == self.faction:
        yield item

  def item_builder(self, parent: ListWidget, index: int, selected: bool):
    return InvestigatorItemWidget(
        parent=parent,
        offset=Offset(parent.item_height * index, 0),
        investigator=self.items[index],
        selected=selected,
    )

  def on_button(self, button: int):
    if button == badger2040.BUTTON_A:
      self.faction = Faction((self.faction - 1) % len(Faction))
      return True
    elif button == badger2040.BUTTON_C:
      self.faction = Faction((self.faction + 1) % len(Faction))
      return True

    return self.list.on_button(button)

  def create_list(self):
    self.items = list(self.faction_items())
    self.list = ListWidget(
        parent=self,
        size=self.size,
        offset=Offset(0, 0),
        item_count=len(self.items),
        item_height=40,
        item_builder=self.item_builder,
        page_item_count=self.page_item_count,
    )

  def render(self):
    super().render()

    self.list.render()
