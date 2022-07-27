import os
import time as t
from pynput.keyboard import Key, Controller

Keyboard=Controller()

os.startfile ("#ADD YOUR APP DIRECTORY HERE")

t.sleep(0.5)

Keyboard.press('')
Keyboard.release('')

Keyboard.press(Key.space)
Keyboard.release(Key.space)

Keyboard.press(Key.enter)
Keyboard.release(Key.enter)