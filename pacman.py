import Tkinter as Tk

class App(object):
    def __init__(self, parent):
        frame = Tk.Frame(parent)
        frame.pack()
        self.label = Tk.Label(frame, text="PACMAN")
        self.label.pack(side=Tk.TOP)
        self.button = Tk.Button(frame, text="GIVE UP", fg="red",
                command=frame.quit)
        self.button.pack(side=Tk.LEFT)
        self.hi_there = Tk.Button(frame, text="HELLO",
                command=self.say_hi)
        self.hi_there.pack(side=Tk.LEFT)

    def say_hi(self):
        print "Hi there, everyone!"

root = Tk.Tk()
app = App(root)
root.mainloop()