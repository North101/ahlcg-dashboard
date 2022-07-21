from typing import TYPE_CHECKING

from ahlcg_dashboard.util import Offset

from .investigator_screen import InvestigatorScreen

if TYPE_CHECKING:
  from .base import App, SizedMixin


class MyApp(App, SizedMixin):
  def __init__(self, **kwargs):
    super().__init__(self, **kwargs)

    self.screen = InvestigatorScreen(
        parent=self,
        size=self.size,
    )

  def on_button(self, button: int):
    return self.screen.on_button(button)

  def render(self):
    super().render()

    self.screen.render()
