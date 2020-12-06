import tkinter as tk

APP_NAME = 'My application Name'
MIN_WIDTH = 300
MIN_HEIGHT = 300


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.set_config()
        self.create_widgets()
        self.pack()

    def set_config(self):
        self.master.wm_title(APP_NAME)
        self.master.wm_minsize(MIN_WIDTH, MIN_HEIGHT)

    def create_widgets(self):
        self.welcomeTitle = tk.Label(self, text='Welcome To My Application')
        self.welcomeTitle.pack(side='top')
        self.translationText = tk.Text(self, wrap=tk.WORD)
        self.translationText.insert(tk.END, 'HAHAHAH')
        self.translationText.pack(side='left')
        self.editText = tk.Entry(self, selectborderwidth=2)
        self.editText.pack(side='right')


root = tk.Tk()
app = Application(master=root)
app.mainloop()
