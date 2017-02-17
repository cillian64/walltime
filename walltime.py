#! /usr/bin/env python3

# Copyright © 2017 David Turner <walltime@dwt27.co.uk>
# This work is free. You can whiteistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import tkinter as tk
from tkinter import font
from datetime import datetime

root = tk.Tk()
root.configure(bg="black")
root.tk_setPalette(background="black", foreground="white")
root.attributes("-fullscreen", True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

small_font = font.Font(family="Ubuntu Mono",
                       size=-int(h/5.5),
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


daylabel = tk.Label(root, text="day", font=small_font)
daylabel.pack()
timelabel = tk.Label(root, text="time", font=big_font)
timelabel.pack(ipady=int((h - h//3 - 2*int(h/5.5))/2))
datelabel = tk.Label(root, text="date", font=small_font)
datelabel.pack()

everysecond(root, daylabel, timelabel, datelabel)

root.mainloop()
