import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import json

class ControlGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Gesture Controller')
        self.start_btn = tk.Button(self.root, text='Start', width=12, command=self._on_start)
        self.stop_btn = tk.Button(self.root, text='Stop', width=12, command=self._on_stop, state='disabled')
        self.load_btn = tk.Button(self.root, text='Load Mapping', width=12, command=self._load_mapping)
        self.start_btn.grid(row=0, column=0, padx=8, pady=8)
        self.stop_btn.grid(row=0, column=1, padx=8, pady=8)
        self.load_btn.grid(row=1, column=0, columnspan=2, padx=8, pady=8)
        self.controller = None
        self.thread = None

    def _on_start(self):
        if not self.controller:
            messagebox.showerror('Error', 'Controller not attached')
            return
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.thread = threading.Thread(target=self.controller.start, daemon=True)
        self.thread.start()

    def _on_stop(self):
        if self.controller:
            self.controller.stop()
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')

    def _load_mapping(self):
        path = filedialog.askopenfilename(filetypes=[('JSON', '*.json')])
        if not path:
            return
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            if self.controller:
                self.controller.mapping = data
            messagebox.showinfo('Loaded', f'Mapping loaded from {path}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def start(self, controller):
        self.controller = controller
        self.root.mainloop()
