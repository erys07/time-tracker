import time


class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.total_time = 0
        self.is_editing = False

    def start_editing(self):
        if self.start_time is None:
            self.start_time = time.time()

    def stop_editing(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            self.total_time += elapsed_time
            self.start_time = None

    def get_total_time(self):
        return self.total_time
