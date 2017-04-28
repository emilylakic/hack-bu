import tkinter as tk

class App(tk.Frame):
    def __init__(self, parent = None):
        super().__init__(parent)
        parent.geometry('500x500')
        self.pack()
        self.add_label()
        self.add_button()
        self.add_slider()

    def add_counter(self):
        self.counter = tk.Label(self, text ='0')
        self.counter.pack()
        self.parent.bind('<Up>', self.inc)

    def inc(self):
        self.counter['text'] = str(1+int(self.counter['text']))

    def add_entry(self):
        self.entry_label = tk.Label(self, text='Input')
        self.entry = tk.Entry(self, bd = 5)
        self.entry_label.pack(side='left')
        self.entry.pack(side='right')
        self.entry.bind('<Return>', self.clear_entry)

    def clear_entry(self, event):
        print(self.entry.get())
        self.entry.delete(0, 'end') #give it the first index in the text that you want to delete (give it 0 to the end)
        print(event)

    def change_text(self):
        self.hello_label['text'] = 'Some new text'
        self.hello_label['fg'] = 'White'
        self.hello_label['bg'] = 'Black'
        print(event)

    def add_label(self):
        self.hello_label = tk.Label(self, text='Hello, World!', font=('Times New Roman', 20))
        self.hello_label.pack(side='bottom')

    def add_button(self):
        self.button = tk.Button(self, text='Change text', command = self.change_text)
        self.button.pack()

    def add_slider(self):
        self.slider = tk.Scale(self, from_= 10, to = 30, orient = tk.HORIZONTAL, command=self.scale_text)
        self.slider.pack()

    def scale_text(self, val):
        self.hello_label.config(font=('Times New Roman', val))

root = tk.Tk()
app = App(parent=root)
app.mainloop()
