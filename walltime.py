#! /usr/bin/env python3

# Copyright © 2017 David Turner <walltime@dwt27.co.uk>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

t = tk.Label(root, text="Hello, Friday!")
t.pack()

root.mainloop()
