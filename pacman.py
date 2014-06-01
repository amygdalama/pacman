import Tkinter as Tk

DIRECTIONS = dict(zip(["Left", "Right", "Up", "Down"],
        [(-10, 0, -10, 0), (10, 0, 10, 0), (0, 10, 0, 10), (0, -10, 0, -10)]))

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black")
        self.frame.bind("<Key>", self.key)
        self.frame.focus_set()
        self.frame.pack()
        self.title = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.title.pack(side=Tk.TOP)
        self.canvas = Tk.Canvas(self.frame, width=200, height=200,
                background="Black")
        self.canvas.pack()
        self.pacman = Pacman(self.canvas)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            self.pacman.move(DIRECTIONS[event.keysym])

class Pacman(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.item_id = self.canvas.create_oval(100, 100, 110, 110,
                fill="Yellow")

    def coords(self):
        return self.canvas.coords(self.item_id)

    def move(self, movement):
        new_coords = tuple(a + b for a, b in zip(self.coords(), movement))
        self.canvas.coords(self.item_id, new_coords)
        print "Pacman moved!"

root = Tk.Tk()
app = App(root)
root.mainloop()