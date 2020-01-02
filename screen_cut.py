from tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.window_init()

    def window_init(self):
        self.master.title('Welcom to Video-Captioning system')
        width,height = self.master.maxsize()
        self.master.geometry('{}x{}'.format(int(width*0.9),int(height*0.9)))

if __name__=='__main__':
    app = Application()
    app.mainloop()

