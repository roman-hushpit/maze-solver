from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title = "Maze solver"
        self.canvas = Canvas(self.root_widget, {"bg": "white"})
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while(self.running) :
            self.redraw()

    
    def close(self):
        self.running = False


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__=="__main__": 
    main() 