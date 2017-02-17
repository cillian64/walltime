#! /usr/bin/env python3

# Copyright © 2017 David Turner <walltime@dwt27.co.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.attributes("-fullscreen", True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()


def everysecond(root, daylabel, timelabel, datelabel):
    now = datetime.now()
    daylabel.configure(text=now.strftime("%A"))
    timelabel.configure(text=now.strftime("%H:%M:%S"))
    datelabel.configure(text=now.strftime("%Y-%m-%d"))
    root.after(1000, everysecond, root, daylabel, timelabel, datelabel)


daylabel = tk.Label(root, text="day")
daylabel.pack()
timelabel = tk.Label(root, text="time")
timelabel.pack()
datelabel = tk.Label(root, text="date")
datelabel.pack()

everysecond(root, daylabel, timelabel, datelabel)

root.mainloop()
