import Tkinter as Tk

DIRECTIONS = set(["Left", "Right", "Up", "Down"])

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black")
        self.frame.bind("<Key>", self.key)
        self.frame.pack()
        self.frame.focus_set()
        self.title = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.title.pack(side=Tk.TOP)
        self.canvas = Tk.Canvas(self.frame, width=200, height=200,
                background="Black")
        self.canvas.pack()
        # self.pacman = Pacman(self.frame)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            print event.keysym

# class Pacman(object):
#     def __init__(self, parent):
#         self.label = Tk.Label(parent, text="P", background="Black",
#                 foreground="Yellow", font="Courier 32")

root = Tk.Tk()
app = App(root)
root.mainloop()