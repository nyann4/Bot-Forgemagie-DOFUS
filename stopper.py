from pynput.keyboard import Listener, Key
import time
import signal
import os

def stopFunction():
    def on_release(key):
        if key == Key.end:
            pid = os.getpid()
            os.kill(pid, signal.SIGTERM)

    with Listener(on_press=lambda k: None, on_release=on_release) as listener:
        listener.join()