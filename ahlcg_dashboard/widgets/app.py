import badger2040
from ahlcg_dashboard.util import Offset, Size

from .base import App, SizedMixin
from .investigator_screen import InvestigatorScreen


class MyApp(App, SizedMixin):
  def __init__(
      self,
      display: badger2040.Badger2040,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset = None,
  ):
    super().__init__(display=display, size=size, clear_color=clear_color, offset=offset)

    self.screen = InvestigatorScreen(
        parent=self,
        size=self.size,
    )

  def on_button(self, pressed: dict[int, bool]):
    return self.screen.on_button(pressed)

  def render(self):
    self.screen.render()
