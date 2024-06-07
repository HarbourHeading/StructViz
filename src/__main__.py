"""Module for visualizing data structures and algorithms"""

import tkinter as tk
from tkinter import HORIZONTAL
import random
import algorithms

window = tk.Tk()
window.minsize(700, 580)

app_width, app_height = 700, 580
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()

mid_x = (screen_width - app_width) // 2
mid_y = (screen_height - app_height) // 2

window.title("StructViz")
window.iconbitmap("./assets/favicon.ico")
window.geometry(f'{app_width}x{app_height}+{mid_x}+{mid_y}')

select_alg = tk.StringVar()
data = []


def regenerate():
    global data

    min_value = int(minEntry.get())
    max_value = int(maxEntry.get())
    amount_value = int(amountEntry.get())

    data = []
    for _ in range(amount_value):
        data.append(random.randint(min_value, max_value + 1))

    draw_data(data, ['Red' for _ in range(len(data))])


def draw_data(algo_data, colorlist):
    structVizC.delete("all")

    canvas_height, canvas_width = 380, 500
    x_width = canvas_width / (len(algo_data) + 1)
    offset, spacing = 30, 10

    normalized_data = [i / max(algo_data) for i in algo_data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 340

        x1 = ((i + 1) * x_width + offset)
        y1 = canvas_height

        structVizC.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        structVizC.create_text(x0 + 2, y0, anchor='se', text=str(algo_data[i]))
    window.update()


def start_algorithm():
    global data

    if navbarLB.curselection():
        algorithmL.config(text=navbarLB.get(navbarLB.curselection()))

        match navbarLB.get(navbarLB.curselection()):
            case "Bubble sort":
                algorithms.bubble(window, data, draw_data, speedbar.get())
            case _:
                pass


window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=45)
window.rowconfigure((0, 1), weight=1)
window.rowconfigure(2, weight=45)

navbarLB = tk.Listbox(window, selectmode=tk.SINGLE)
for item in ["Bubble sort", "Option 2", "Option 3"]:
    navbarLB.insert(tk.END, item)
navbarLB.grid(row=0, column=0, rowspan=3, sticky='nsew')

userSettingsF = (tk.Frame(window, background='bisque2')
                 .grid(row=0, column=1, columnspan=2, rowspan=2, sticky='news', padx=7, pady=5))

algorithmL = tk.Label(userSettingsF, text='No algorithm selected', background='bisque2')
algorithmL.grid(row=0, column=1, sticky='nw', padx=10, pady=10)

space_notation_l = tk.Label(userSettingsF, text='Time notation: ', background='bisque2')
space_notation_l.grid(row=0, column=1, sticky='sw', padx=10, pady=10)

amountEntry = tk.Scale(userSettingsF, from_=5, to=40, label='Amount', background='bisque2',
                       orient=HORIZONTAL, resolution=1, cursor='arrow')
amountEntry.grid(row=0, column=1, sticky='n', padx=10, pady=10)

minEntry = tk.Scale(userSettingsF, from_=0, to=10, resolution=1, background='bisque2',
                    orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, sticky='s', padx=10, pady=10)

maxEntry = tk.Scale(userSettingsF, from_=10, to=100, resolution=1, background='bisque2',
                    orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=1, sticky='se', padx=10, pady=10)

speedbar = tk.Scale(userSettingsF, from_=0.10, to=2.0, length=100, digits=2, background='bisque2',
                    resolution=0.1, orient=HORIZONTAL, label="Speed")
speedbar.grid(row=0, column=1, sticky='ne', padx=10, pady=10)

tk.Button(userSettingsF, text="Start", bg="Blue", command=start_algorithm, background='bisque2').grid(
    row=1, column=1, sticky='nw', padx=10, pady=10)

tk.Button(userSettingsF, text="Regenerate", bg="Red", command=regenerate, background='bisque2').grid(
    row=1, column=1, sticky='sw', padx=10, pady=10)

structVizC = tk.Canvas(window, background='bisque2')
structVizC.grid(row=2, column=1, sticky='news', padx=5, pady=5)

window.mainloop()
