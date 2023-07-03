"""

Watermark project
#100Days of Code with Python
Day: 84
Date: 2023-07-01
Author: MC

"""

import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from TextWatermark.TextWatermark import TextWatermark as twm

# ---------------------------- CONSTANTS ------------------------------- #
BG_COLOR = '#787878'

text_wm = twm()

# ---------------------------- SELECT FILE FUNC ------------------------ #


def select_file():
    filetype = (
        ('image files - jpg', '*.jpg'),
        ('image files - png', '*.png'),
        ('all files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetype
    )

    showinfo(
        title="Selected files",
        message=filename
    )

    return filename


# ---------------------------- UI SETUP ------------------------------- #

# init window
window = tk.Tk()
window.title('Portfolio - Watermark by MC')
window.minsize(width=800, height=600)
window['bg'] = BG_COLOR
# window.config(padx=50, pady=50)
# window['bg'] = "#787878"

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# title label
title_label = tk.Label(
    text="Watermark maker by MC",
    font=("Arial bold", 32),
    fg='Black',
    bg=BG_COLOR)
title_label.grid(
    row=0,
    column=0,
    columnspan=2
)

# watermark section
watermark_title_label = tk.Label(
    text="Watermark section",
    font=('Arial bold', 24),
    fg='black',
    bg=BG_COLOR
)
watermark_title_label.grid(
    row=1,
    column=0)

watermark_text_label = tk.Label(
    text="Please enter text below:",
    font=("Arial", 18),
    fg='white',
    bg=BG_COLOR
)
watermark_text_label.grid(
    row=2,
    column=0
)

watermark_entries = tk.Entry(width=40)
watermark_entries.insert(tk.END, string='Please enter text')
watermark_entries.grid(
    row=3,
    column=0
)

# image section
image_sec_title_label = tk.Label(
    text="Image section",
    font=('Arial bold', 24),
    fg='black',
    bg=BG_COLOR
)
image_sec_title_label.grid(
    row=1,
    column=1
)

image_sec_select_label = tk.Label(
    text="Select image:",
    font=('Arial', 18),
    fg='white',
    bg=BG_COLOR
)
image_sec_select_label.grid(
    row=2,
    column=1
)

# open file dialog - button
image_sec_open_button = tk.Button(
    window,
    text="Open file",
    bg=BG_COLOR,
    command=select_file
)

image_sec_open_button.grid(
    row=3,
    column=1
)





# main loop to run app
window.mainloop()
