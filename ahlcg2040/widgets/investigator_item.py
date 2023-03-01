from ahlcg2040.data import Investigator
from badger_ui import App, Offset, Size, Widget
from badger_ui.list import ListWidget


class InvestigatorItemWidget(Widget):
  parent: ListWidget

  def __init__(self, investigator: Investigator, selected: bool):
    self.investigator = investigator
    self.selected = selected

  def render(self, app: App, size: Size, offset: Offset):
    app.display.set_pen(0)
    if self.selected:
      app.display.rectangle(
          offset.x,
          offset.y,
          size.width,
          size.height,
      )
      app.display.set_pen(15)
    app.display.set_thickness(2)
    app.display.text(
        self.investigator.name,
        offset.x + 2,
        offset.y + (size.height // 2),
        scale=0.8,
    )
