import Tkinter as Tk

DIRECTIONS = set(["Left", "Right", "Up", "Down"])

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black",
                width=800, height=800)
        self.frame.bind("<Key>", self.key)
        self.frame.pack()
        self.frame.focus_set()
        self.label = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.label.pack(side=Tk.TOP)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            print event.keysym

root = Tk.Tk()
app = App(root)
root.mainloop()