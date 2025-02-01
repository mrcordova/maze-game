from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        # self.width = width
        # self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__canvas = Canvas(self.__root_widget, bg='white', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False
        self.__root_widget.protocol('WM_DELETE_WINDOW', self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_fo_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
    def close(self):
        self.__window_running = False


        