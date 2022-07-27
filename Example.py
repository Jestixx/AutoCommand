import os
import time as t
from pynput.keyboard import Key, Controller

Keyboard=Controller()

os.startfile ("C:\Windows\system32\cmd.exe")

t.sleep(0.5)

Keyboard.press('M')
Keyboard.release('M')

Keyboard.press('S')
Keyboard.release("S")

Keyboard.press("G")
Keyboard.release('G')

Keyboard 

Keyboard.press(Key.space)
Keyboard.release(Key.space)

Keyboard.press("*")
Keyboard.release("*")

Keyboard.press(Key.space)
Keyboard.release(Key.space)

Keyboard.press("H")
Keyboard.release("H")

Keyboard.press("i")
Keyboard.release("i")

Keyboard.press(Key.enter)
Keyboard.release(Key.enter)
