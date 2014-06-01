import Tkinter as Tk

PACMAN_SIZE = 30
CANVAS_SIZE = PACMAN_SIZE*3
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
        self.maze = Maze(self.canvas)
        self.pacman = Pacman(self.canvas, self.maze)

    def key(self, event):
        if event.keysym in DIRECTIONS:
            self.pacman.move(DIRECTIONS[event.keysym])

class Pacman(object):
    def __init__(self, canvas, maze):
        self.canvas = canvas
        self.maze = maze
        self.item_id = self.canvas.create_oval(PACMAN_SIZE, 0,
            PACMAN_SIZE*2, PACMAN_SIZE, fill="Yellow")

    def coords(self):
        return self.canvas.coords(self.item_id)

    def move(self, movement):
        current_coords = self.coords()
        new_x = (current_coords[0] + movement[0]) % CANVAS_SIZE
        new_y = (current_coords[1] + movement[1]) % CANVAS_SIZE
        new_coords = (new_x, new_y, new_x + PACMAN_SIZE,
                new_y + PACMAN_SIZE)
        if not self.maze.is_wall(new_coords):
            self.canvas.coords(self.item_id, new_coords)
        self.maze.eat_pellets(new_coords)

class Maze(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.line_width = 5
        self.walls = self.draw_walls(self.canvas)
        self.pellets = self.add_pellets()

    def draw_walls(self, canvas):
        walls = set()
        offset = PACMAN_SIZE-self.line_width
        walls.add(self.canvas.create_line(offset, 0,
                offset, CANVAS_SIZE,
                fill="Blue", width=5))
        walls.add(self.canvas.create_line(CANVAS_SIZE-offset, 0,
                CANVAS_SIZE-offset, CANVAS_SIZE, fill="Blue", width=5))
        self.canvas.addtag_all("wall")
        return walls

    def is_wall(self, coords):
        things = set(self.canvas.find_overlapping(*coords))
        if things.intersection(self.walls):
            return True
        else:
            return False

    def add_pellets(self):
        pellets = set()
        for i in xrange(0, 3):
            y1 = PACMAN_SIZE*.5 + i*PACMAN_SIZE
            y2 = y1 + .5*PACMAN_SIZE
            pellet = self.canvas.create_oval(PACMAN_SIZE*1.25,
                    y1, PACMAN_SIZE*1.75, y2, fill="White")
            pellets.add(pellet)
            self.canvas.itemconfig(pellet, tags="pellet")
        return pellets

    def eat_pellets(self, coords):
        things = set(self.canvas.find_overlapping(*coords))
        pellets = things.intersection(self.pellets)
        for pellet in pellets:
            self.canvas.delete(pellet)


if __name__ == '__main__':
    root = Tk.Tk()
    app = App(root)
    root.mainloop()