#! /usr/bin/env python3

# Copyright © 2017 David Turner <walltime@dwt27.co.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import tkinter as tk
from tkinter import font
from datetime import datetime

root = tk.Tk()
root.attributes("-fullscreen", True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

small_font = font.Font(family="Ubuntu Mono",
                       size=-(h//5),
                       weight="bold")
big_font = font.Font(family="DSEG7 Modern",
                     size=-(h//3),
                     weight="bold")


def everysecond(root, daylabel, timelabel, datelabel):
    now = datetime.now()
    daylabel.configure(text=now.strftime("%A"))
    timelabel.configure(text=now.strftime("%H:%M"))
    datelabel.configure(text=now.strftime("%Y-%m-%d"))
    root.after(1000, everysecond, root, daylabel, timelabel, datelabel)


daylabel = tk.Label(root, text="day",
                    relief=tk.RIDGE,
                    font=small_font)
daylabel.grid(row=0, column=0)
timelabel = tk.Label(root, text="time", relief=tk.RIDGE,
                     font=big_font)
timelabel.grid(row=1, column=0)
datelabel = tk.Label(root, text="date", relief=tk.RIDGE,
                     font=small_font)
datelabel.grid(row=2, column=0)

everysecond(root, daylabel, timelabel, datelabel)

root.mainloop()
