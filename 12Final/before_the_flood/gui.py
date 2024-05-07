import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.font import Font
from pygame import mixer


def create_gui():
    window = tk.Tk()
    window.title("Before The Flood")

    output_box = scrolledtext.ScrolledText(master=window, wrap="word", height=50, width=120, font=Font(family="Courier", size=14))
    output_box.pack(fill="both", expand=True)

    output_box.tag_configure("bold", font=Font(family="Courier", size=14, weight='bold'))
    output_box.tag_configure("title", font=Font(family='Courier', size=18, weight='bold')) 
    output_box.tag_configure("red", foreground="red")
    output_box.tag_configure("green", foreground="green")
    output_box.tag_configure("blue", foreground="blue")

    input_box = ttk.Entry(master=window, width=90)
    input_box.pack(fill="x", padx=30)
    
    mixer.init()


    return window, output_box, input_box

