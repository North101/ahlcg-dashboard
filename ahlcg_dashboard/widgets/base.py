from typing import Generic, Optional, TypeVar

import badger2040
from ahlcg_dashboard.buttons import ButtonHandler
from ahlcg_dashboard.util import Offset, Size


class WidgetMixin:
  app: 'WidgetMixin'
  display: badger2040.Badger2040
  offset: Offset

  def on_button(self, button: int) -> bool:
    raise NotImplementedError()

  def render(self):
    raise NotImplementedError()


T = TypeVar('T', bound=WidgetMixin)


class Widget(WidgetMixin, Generic[T]):
  def __init__(self, parent: T, offset: Offset):
    self.parent = parent
    self._offset = offset

  @property
  def app(self) -> 'App':
    return self.parent.app

  @property
  def offset(self):
    return self.parent.offset + self._offset

  @property
  def display(self):
    return self.parent.display


class SizedMixin:
  size: Size


class App(WidgetMixin, SizedMixin):
  def __init__(
      self,
      display=badger2040.Badger2040(),
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      offset=Offset(0, 0),
      clear_color: int = 15,
  ):
    self.display = display
    self.size = size
    self.offset = offset
    self.screen: Optional[WidgetMixin] = None
    self.buttons = ButtonHandler(self.on_button)
    self.clear_color = clear_color

  @property
  def app(self):
    return self
  
  def clear(self):
    self.display.pen(self.clear_color)
    self.display.clear()

  def __call__(self):
    self.clear()
    self.render()
    self.display.update()