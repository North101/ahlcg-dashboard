import badger2040
from machine import Pin


class ButtonCallback:
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

  def __eq__(self, other):
    if isinstance(other, Button):
      return self == other
    elif isinstance(other, Pin):
      return self.pin == other
    return False


class ButtonHandler:
  buttons = {
      badger2040.BUTTON_A: Button(badger2040.BUTTON_A, invert=False),
      badger2040.BUTTON_B: Button(badger2040.BUTTON_B, invert=False),
      badger2040.BUTTON_C: Button(badger2040.BUTTON_C, invert=False),
      badger2040.BUTTON_UP: Button(badger2040.BUTTON_UP, invert=False),
      badger2040.BUTTON_DOWN: Button(badger2040.BUTTON_DOWN, invert=False),
      badger2040.BUTTON_USER: Button(badger2040.BUTTON_USER),
  }

  def __init__(self):
    self.pressed = None
    for button in self.buttons.values():
      button.irq(self.handler)

  def handler(self, pin: int):
    self.pressed = pin

  def __getitem__(self, pin: int):
    return self.buttons[pin]
