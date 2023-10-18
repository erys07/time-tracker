import tkinter as tk
import program_detection
import input_monitoring
from time_tracking import TimeTracker
from datetime import datetime
from teste import TimerApp

root = tk.Tk()

tracker = TimeTracker()
start_time = None
teste = TimerApp(root)


def check_editor_and_input():
    global start_time
    if program_detection.is_davinci_open() and input_monitoring.input_detector.is_input_active:
        if not tracker.is_editing:
            tracker.start_editing()
            teste.start_timer()
        if start_time is None:
            start_time = datetime.now()
    else:
        teste.stop_timer()
        if start_time is not None:
            end_time = datetime.now()
            elapsed_time = end_time - start_time
            start_time = None

    root.after(1000, check_editor_and_input)


check_editor_and_input()

root.mainloop()
