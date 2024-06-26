"""Module for visualizing data structures and algorithms"""


import tkinter as tk
from random import randint
from sys import exit
from tkinter import HORIZONTAL, font

from _tkinter import TclError

import algorithms


class App(tk.Tk):
    data: list[int] = []

    def __init__(self) -> None:
        super().__init__()

        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.config(family="Arial")

        self.navbar = tk.Listbox(self, selectmode=tk.SINGLE, activestyle='none')
        for item in ["Bubble sort", "Quick sort", "Merge sort"]:
            self.navbar.insert(tk.END, item)

        self.user_settings = tk.Frame(self, background='bisque2')
        self.algorithm = tk.Label(self.user_settings, text='Algorithm: ', background='bisque2')
        self.time_complexity = tk.Label(self.user_settings, text='Time complexity: ', background='bisque2')
        self.input_size = tk.Scale(self.user_settings, from_=5, to=60, label='Amount', background='bisque2',
                                   orient=HORIZONTAL, resolution=1, cursor='arrow')
        self.sort_speed = tk.Scale(self.user_settings, from_=0.01, to=2.0, resolution=0.01, background='bisque2',
                                   orient=HORIZONTAL, label="Speed", length=100, digits=3)
        self.start_button = tk.Button(self.user_settings, text="Start", command=self.start_algorithm,
                                      background='bisque2')
        self.regen_button = tk.Button(self.user_settings, text="Regenerate", command=self.regenerate,
                                      background='bisque2')
        self.min_entry = tk.Scale(self.user_settings, from_=0, to=10, resolution=1, background='bisque2',
                                  orient=HORIZONTAL, label="Minimum Value")
        self.max_entry = tk.Scale(self.user_settings, from_=10, to=100, resolution=1, background='bisque2',
                                  orient=HORIZONTAL, label="Maximum Value")
        self.sort_canvas = tk.Canvas(self, background='bisque2')

        self.configure_root()

        self.mainloop()

    def configure_root(self) -> None:
        """Initialize the root window"""

        self.minsize(700, 580)
        app_width, app_height = 700, 580
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()

        mid_screen_x = (screen_width - app_width) // 2
        mid_screen_y = (screen_height - app_height) // 2

        self.title("StructViz")
        self.iconbitmap("./assets/favicon.ico")
        self.geometry(f'{app_width}x{app_height}+{mid_screen_x}+{mid_screen_y}')

        self.columnconfigure(0, weight=1)
        self.columnconfigure((1, 2, 3), weight=45)
        self.rowconfigure((0, 1), weight=1)
        self.rowconfigure(2, weight=45)

        self.navbar.grid(row=0, column=0, rowspan=3, sticky='nsew')
        self.user_settings.grid(row=0, column=1, columnspan=3, rowspan=2, sticky='news', padx=7, pady=5)
        self.algorithm.grid(row=0, column=1, sticky='nw', padx=10, pady=10)
        self.time_complexity.grid(row=0, column=1, sticky='sw', padx=10, pady=10)
        self.input_size.grid(row=0, column=2, padx=10, pady=10)
        self.sort_speed.grid(row=0, column=3, padx=10, pady=10)
        self.start_button.grid(row=1, column=1, sticky='nw', padx=10, pady=10)
        self.regen_button.grid(row=1, column=1, sticky='sw', padx=10, pady=10)
        self.min_entry.grid(row=1, column=2, padx=10, pady=10)
        self.max_entry.grid(row=1, column=3, padx=10, pady=10)
        self.sort_canvas.grid(row=2, column=1, columnspan=3, sticky='news', padx=5, pady=5)

    def start_algorithm(self) -> None:
        """Start sorting process"""

        if not self.navbar.curselection():  # No algorithm from navbar selected
            return

        self.start_button.config(text='Paused', state='disabled')
        self.regen_button.config(state='disabled')
        self.algorithm.config(text="Algorithm: " + self.navbar.get(self.navbar.curselection()))

        speed = float(self.sort_speed.get())

        match self.navbar.get(self.navbar.curselection()):
            case "Bubble sort":
                self.time_complexity.config(text="Time complexity: O(n^2)")
                algorithms.bubble_sort_algorithm(self.data, self.draw_data, speed)

            case "Quick sort":
                self.time_complexity.config(text="Time complexity: O(n^2)")
                algorithms.quick_sort_algorithm(self.data, self.draw_data, 0, len(self.data) - 1, speed)

            case "Merge sort":
                self.time_complexity.config(text="Time complexity: O(n*log(n))")
                algorithms.merge_sort_algorithm(self.data, self.draw_data, 0, len(self.data) - 1, speed)

            case _:  # In case of unexpected behaviour
                pass

        self.start_button.config(text='Start', state='normal')
        self.regen_button.config(state='normal')

        self.draw_data(self.data, ['Green'] * len(self.data))

    def regenerate(self) -> None:

        min_value = int(self.min_entry.get())
        max_value = int(self.max_entry.get())
        input_value = int(self.input_size.get())

        self.data = []
        for _ in range(input_value):
            self.data.append(randint(min_value, max_value))

        self.draw_data(self.data, ['Red'] * len(self.data))

    def draw_data(self, data: list[int], color: list[str]) -> None:
        try:
            self.sort_canvas.delete('all')
        except TclError:  # Canvas does not exist (e.g. program was closed during the sorting process)
            exit()

        canvas_height, canvas_width = 380, 500
        x_width = canvas_width / (len(data) + 1)
        offset, spacing = 30, 10

        normalized_data = [i / max(data) for i in data]

        for i, height in enumerate(normalized_data):
            x_0 = i * x_width + offset + spacing
            y_0 = canvas_height - height * 340

            x_1 = ((i + 1) * x_width + offset)
            y_1 = canvas_height

            self.sort_canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=color[i])
            self.sort_canvas.create_text(x_0 + 2, y_0, anchor='se', text=str(data[i]))
        self.update()
