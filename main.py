"""
AutoClicker - Toggle with F6 (or your chosen hotkey)
Requirements: pip install pynput
"""

import time
import threading
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, HotKey, Listener as KeyboardListener

TOGGLE_KEY    = Key.f6          
CLICK_BUTTON  = Button.left     
CLICKS_PER_SECOND = 10          

mouse_ctrl = MouseController()
clicking   = False
stop_flag  = False


def click_loop():
    interval = 1.0 / CLICKS_PER_SECOND
    while not stop_flag:
        if clicking:
            mouse_ctrl.click(CLICK_BUTTON)
            time.sleep(interval)
        else:
            time.sleep(0.01)  


def on_press(key):
    global clicking, stop_flag
    if key == TOGGLE_KEY:
        clicking = not clicking
        state = "ON  🟢" if clicking else "OFF 🔴"
        print(f"\r  AutoClicker: {state}   ", end="", flush=True)
    elif key == Key.esc:
        print("\n  ESC pressed — exiting.")
        stop_flag = True
        return False   


def main():
    print("=" * 42)
    print("  AutoClicker ready!")
    print(f"  Toggle : {TOGGLE_KEY}")
    print(f"  Button : {CLICK_BUTTON}")
    print(f"  Speed  : {CLICKS_PER_SECOND} CPS")
    print("  Quit   : ESC")
    print("=" * 42)
    print(f"\r  AutoClicker: OFF 🔴   ", end="", flush=True)

    clicker_thread = threading.Thread(target=click_loop, daemon=True)
    clicker_thread.start()

    with KeyboardListener(on_press=on_press) as listener:
        listener.join()

    print()   


if __name__ == "__main__":
    main()