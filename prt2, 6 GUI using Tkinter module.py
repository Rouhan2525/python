import tkinter as tk
w = tk.Tk()
w.title("GUI EXAMPLE")
w.geometry("600x400")
label = tk.Label(w,text = "welcome to AIMCA ,bhatkal .by using Tkinter")
label.pack()
button = tk.Button(w,text = "click me!",command =w.destroy)
button.pack()
w.mainloop()