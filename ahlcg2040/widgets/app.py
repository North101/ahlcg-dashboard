from badger_ui import App

from .investigator_screen import InvestigatorScreen


class MyApp(App):
  def __init__(self):
    super().__init__()

    self.child = InvestigatorScreen()
