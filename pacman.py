import Tkinter as Tk

PACMAN_SIZE = 30
CANVAS_SIZE = PACMAN_SIZE*20
DIRECTIONS = dict(zip(["Left", "Right", "Up", "Down"],
        [(-PACMAN_SIZE, 0, -PACMAN_SIZE, 0), (PACMAN_SIZE, 0, PACMAN_SIZE, 0),
        (0, -PACMAN_SIZE, 0, -PACMAN_SIZE), (0, PACMAN_SIZE, 0, PACMAN_SIZE)]))

class App(object):
    def __init__(self, parent):
        self.frame = Tk.Frame(parent, background="Black")
        self.frame.bind("<Key>", self.key)
        self.frame.focus_set()
        self.frame.pack()
        self.title = Tk.Label(self.frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.title.pack(side=Tk.TOP)
        self.canvas = Tk.Canvas(self.frame, width=CANVAS_SIZE,
                height=CANVAS_SIZE, background="Black")
        self.canvas.pack()
        self.pacman = Pacman(self.canvas)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            self.pacman.move(DIRECTIONS[event.keysym])

class Pacman(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.item_id = self.canvas.create_oval(CANVAS_SIZE/2, CANVAS_SIZE/2,
            CANVAS_SIZE/2 + PACMAN_SIZE, CANVAS_SIZE/2 + PACMAN_SIZE,
            fill="Yellow")

    def coords(self):
        return self.canvas.coords(self.item_id)

    def move(self, movement):
        new_coords = tuple(a + b for a, b in
                zip(self.coords(), movement))
        # for a, b in zip(self.coords(), movement):
        #     if a ==
        # print new_coords
        self.canvas.coords(self.item_id, new_coords)

root = Tk.Tk()
app = App(root)
root.mainloop()