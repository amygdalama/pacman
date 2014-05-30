import Tkinter as Tk

class App(object):
    def __init__(self, parent):
        frame = Tk.Frame(parent, background="Black")
        frame.pack()
        self.label = Tk.Label(frame, text="PACMAN", background="Black",
                foreground="White", font="Courier 32")
        self.label.pack(side=Tk.TOP)
        self.button = Tk.Button(frame, text="GIVE UP",
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