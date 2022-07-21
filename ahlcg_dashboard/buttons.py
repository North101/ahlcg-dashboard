from typing import Protocol

import badger2040
from machine import Pin


class ButtonCallback(Protocol):
  def __call__(self, pin: int):
    pass


class Button:
  def __init__(self, id: int, invert: bool = True):
    self.id = id
    self.pin = Pin(id, Pin.IN, Pin.PULL_UP if invert else Pin.PULL_DOWN)

  def irq(self, handler: ButtonCallback):
    self.pin.irq(trigger=Pin.IRQ_RISING, handler=handler)

  def value(self):
    return self.pin.value()


class ButtonHandler:
  buttons = {
      badger2040.BUTTON_A: Button(badger2040.BUTTON_A, invert=False),
      badger2040.BUTTON_B: Button(badger2040.BUTTON_B, invert=False),
      badger2040.BUTTON_C: Button(badger2040.BUTTON_C, invert=False),
      badger2040.BUTTON_UP: Button(badger2040.BUTTON_UP, invert=False),
      badger2040.BUTTON_DOWN: Button(badger2040.BUTTON_DOWN, invert=False),
      badger2040.BUTTON_USER: Button(badger2040.BUTTON_USER),
  }

  def __init__(self, on_button: ButtonCallback):
    for button in self.buttons.values():
      button.irq(on_button)

  def __getitem__(self, pin: int):
    return self.buttons[pin]
