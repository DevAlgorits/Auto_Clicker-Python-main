import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

### tecla "x" para habilitiar e desabilitar auto-clicker
TOGGLE_KEY = KeyCode(char = "x") 

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.0001) # valor para frequencia de click


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target = clicker)
click_thread.start()

with Listener(on_press = toggle_event) as listener:
    listener.join()
