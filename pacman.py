import Tkinter as Tk

DIRECTIONS = set(["Left", "Right", "Up", "Down"])

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black")
        self.frame.pack()
        self.title = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.title.pack(side=Tk.TOP)
        self.canvas = Tk.Canvas(self.frame, width=200, height=200,
                background="Black")
        self.canvas.pack()
        self.pacman = Pacman(self.canvas)

class Pacman(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.pacman = self.canvas.create_oval(100, 100, 110, 110,
                fill="Yellow")
        self.canvas.tag_bind(self.pacman, '<Key>', self.key)
        self.canvas.focus_set()
        self.canvas.focus(self.pacman)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            print event.keysym

root = Tk.Tk()
app = App(root)
root.mainloop()