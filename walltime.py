import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

t = tk.Label(root, text="Hello, Friday!")
t.pack()

root.mainloop()
