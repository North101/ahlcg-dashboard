from typing import Generic, Optional, TypeVar

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

  def on_button(self, button: int) -> bool:
    raise NotImplementedError()

  def render(self):
    raise NotImplementedError()


T = TypeVar('T', bound=WidgetMixin)


class Widget(WidgetMixin, Generic[T]):
  def __init__(self, parent: T, offset: Optional[Offset]):
    self.parent = parent
    self.offset = offset or Offset(0, 0)

  @property
  def app(self) -> 'App':
    return self.parent.app
  
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
      display=badger2040.Badger2040(),
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Optional[Offset] = None,
  ):
    self.display = display
    self.size = size
    self.offset = offset or Offset(0, 0)
    self.screen: Optional[WidgetMixin] = None
    self.buttons = ButtonHandler(self.on_button)
    self.clear_color = clear_color
    self.dirty = True

  @property
  def app(self):
    return self

  def on_button(self, button: int) -> bool:
    result = super().on_button(button)
    self.dirty = self.dirty or result
    
    return result

  def clear(self):
    self.display.pen(self.clear_color)
    self.display.clear()

  def update(self):
    if not self.dirty:
      return

    self.clear()
    self.render()
    self.display.update()
