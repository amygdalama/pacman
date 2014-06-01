import Tkinter as Tk

SIZE = 30
DIRECTIONS = dict(zip(["Left", "Right", "Up", "Down"],
        [(-SIZE, 0, -SIZE, 0), (SIZE, 0, SIZE, 0),
        (0, -SIZE, 0, -SIZE), (0, SIZE, 0, SIZE)]))

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black")
        self.frame.bind("<Key>", self.key)
        self.frame.focus_set()
        self.frame.pack()
        self.title = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.title.pack(side=Tk.TOP)
        self.canvas = Tk.Canvas(self.frame, width=SIZE*20, height=SIZE*20,
                background="Black")
        self.canvas.pack()
        self.pacman = Pacman(self.canvas)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            self.pacman.move(DIRECTIONS[event.keysym])

class Pacman(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.item_id = self.canvas.create_oval(SIZE*10, SIZE*10,
            SIZE*10+SIZE, SIZE*10+SIZE, fill="Yellow")

    def coords(self):
        return self.canvas.coords(self.item_id)

    def move(self, movement):
        new_coords = tuple(a + b for a, b in zip(self.coords(), movement))
        self.canvas.coords(self.item_id, new_coords)

root = Tk.Tk()
app = App(root)
root.mainloop()