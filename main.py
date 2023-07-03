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
from tkinter import ttk

from TextWatermark.TextWatermark import TextWatermark as twm

# ---------------------------- CONSTANTS ------------------------------- #
BG_COLOR = '#787878'
LABEL_FONT_32 = ('NewYork', 32)
LABEL_FONT_24 = ('NewYork', 24)
LABEL_FONT_18 = ('NewYork', 18)

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

# title label
title_label = tk.Label(
    text="Watermark maker by MC",
    font=LABEL_FONT_32,
    fg='Black',
    bg=BG_COLOR
)
title_label.pack()

# separator
sep_style = ttk.Style()
sep_style.configure('blue.TSeparator', background='blue')

sep01 = ttk.Separator(
    window,
    orient='horizontal',
    style='blue.TSeparator'
)
sep01.pack(fill='x')

# walić to nie będzie separatora :(

# watermark sectoion
watermark_section_label = tk.Label(
    text="Watermark section",
    font=LABEL_FONT_24,
    fg='black',
    bg=BG_COLOR
)
watermark_section_label.pack()

# watermark_title_label
watermark_title_label = tk.Label(
    text="Please enter text below:",
    font=LABEL_FONT_18,
    fg='white',
    bg=BG_COLOR
)
watermark_title_label.pack()

# watermark entries
watermark_entries = tk.Entry(width=75)
watermark_entries.pack()

# maybe someday in this place will be separator

# image section
image_title_section = tk.Label(
    text="Image section",
    font=LABEL_FONT_24,
    fg='black',
    bg=BG_COLOR
)
image_title_section.pack()

# image_section_label
image_section_label = tk.Label(
    text="Select image:",
    font=LABEL_FONT_18,
    fg='white',
    bg=BG_COLOR
)
image_section_label.pack()

# open file dialog
image_sec_open_button = tk.Button(
    window,
    text="Open file",
    bg=BG_COLOR,
    command=select_file
)
image_sec_open_button.pack()


# main loop to run app
window.mainloop()
