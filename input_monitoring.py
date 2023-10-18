from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import threading


class InputDetector:
    def __init__(self):
        self.is_input_active = False
        self.inactivity_timeout = 1
        self.inactivity_timer = None

    def on_mouse_move(self, x, y):
        self.is_input_active = True
        self.reset_inactivity_timer()

    def on_key_press(self, key):
        self.is_input_active = True
        self.reset_inactivity_timer()

    def on_key_release(self, key):
        self.is_input_active = True
        self.reset_inactivity_timer()

    def reset_inactivity_timer(self):
        if self.inactivity_timer is not None:
            self.inactivity_timer.cancel()
        self.inactivity_timer = threading.Timer(self.inactivity_timeout, self.set_input_inactive)
        self.inactivity_timer.start()

    def set_input_inactive(self):
        self.is_input_active = False


input_detector = InputDetector()
mouse_listener = MouseListener(on_move=input_detector.on_mouse_move)
keyboard_listener = KeyboardListener(on_press=input_detector.on_key_press, on_release=input_detector.on_key_release)

mouse_listener.start()
keyboard_listener.start()
