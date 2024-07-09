import tkinter as tk
from pynput import mouse
from collections import defaultdict
import threading
import time

class MouseTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Position Tracker")
        
        self.label = tk.Label(self.root, text="Move the mouse and triple click to log coordinates", font=("Helvetica", 14))
        self.label.pack(pady=20)
        
        self.coord_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.coord_label.pack(pady=10)
        
        self.log_box = tk.Text(self.root, width=50, height=10, font=("Helvetica", 12))
        self.log_box.pack(pady=20)
        
        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click)
        self.listener.start()

        self.click_times = defaultdict(list)
        self.click_positions = defaultdict(list)
        
        self.check_triple_click_thread = threading.Thread(target=self.check_triple_click)
        self.check_triple_click_thread.daemon = True
        self.check_triple_click_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_move(self, x, y):
        self.coord_label.config(text=f"Current position: ({x}, {y})")

    def on_click(self, x, y, button, pressed):
        if pressed:
            current_time = time.time()
            self.click_times[button].append(current_time)
            self.click_positions[button].append((x, y))
            self.click_times[button] = self.click_times[button][-3:]
            self.click_positions[button] = self.click_positions[button][-3:]
    
    def check_triple_click(self):
        while True:
            time.sleep(0.1)
            for button in self.click_times:
                if len(self.click_times[button]) == 3 and (self.click_times[button][2] - self.click_times[button][0]) <= 0.5:
                    x, y = self.click_positions[button][0]
                    self.log_box.insert(tk.END, f"Triple clicked at: ({x}, {y})\n")
                    self.click_times[button] = []
                    self.click_positions[button] = []

    def on_closing(self):
        self.listener.stop()
        self.root.destroy()

if __name__ == "__main__":
    MouseTracker()
