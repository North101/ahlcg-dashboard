import badger2040
from ahlcg_dashboard.buttons import ButtonHandler
from ahlcg_dashboard.util import Offset, Size


class WidgetMixin:
  app: 'WidgetMixin'
  display: badger2040.Badger2040
  offset: Offset

  @property
  def display_offset(self):
    return self.offset

  def on_button(self, pressed: dict[int, bool]) -> bool:
    return False

  def render(self):
    pass


class Widget(WidgetMixin):
  def __init__(self, parent: WidgetMixin, offset: Offset = None):
    self.parent = parent
    self.offset = offset or Offset(0, 0)

  @property
  def app(self) -> 'App':
    return self.parent.app

  @property
  def buttons(self):
    return self.app.buttons

  @property
  def dirty(self):
    return self.dirty

  @dirty.setter
  def dirty(self, value: bool):
    self.app.dirty = value

  @property
  def display_offset(self):
    return self.parent.display_offset + self.offset

  @property
  def display(self):
    return self.parent.display


class SizedMixin:
  size: Size


class App(WidgetMixin, SizedMixin):
  def __init__(
      self,
      display: badger2040.Badger2040,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset = None,
  ):
    self.display = display
    self.size = size
    self.offset = offset or Offset(0, 0)
    self.screen: WidgetMixin = None
    self.buttons = ButtonHandler()
    self.clear_color = clear_color
    self.dirty = True

  @property
  def app(self):
    return self

  def test_button(self) -> bool:
    result = self.on_button(self.buttons.pressed())
    self.dirty = self.dirty or result

    return result

  def clear(self):
    self.display.pen(self.clear_color)
    self.display.clear()

  def update(self):
    if self.buttons.dirty:
      self.test_button()
      self.buttons.dirty = False

    if not self.dirty:
      return

    self.clear()
    self.render()
    for _ in range(2):
      self.display.update()
    self.dirty = False
    self.display.halt()
