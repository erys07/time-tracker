import tkinter as tk
from datetime import datetime, timedelta


def format_time(time_delta):
    hours, remainder = divmod(time_delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'


class TimerApp:
    def __init__(self, parent):
        self.root = parent
        self.root.title("Contador de Tempo")

        self.elapsed_time = timedelta(0)

        self.label = tk.Label(parent, text="00:00:00", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)

        self.is_running = False
        self.start_time = None

    def update_timer(self):
        if self.is_running:
            current_time = datetime.now()
            elapsed_time = current_time - self.start_time
            self.elapsed_time += elapsed_time
            self.start_time = current_time
            formatted_time = format_time(self.elapsed_time)
            self.label.config(text=formatted_time)
        self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update_timer()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_time = None
