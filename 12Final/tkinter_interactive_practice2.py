import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = Image.open("/Users/timburns/Documents/GitHub/itp/12Final/before_the_flood/assets/images/Prologue1.png")
    image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.itemconfig(image_id, image=photo)
    canvas.image = photo

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container, width=900, height=700)
canvas.bind("<Configure>", resize_image)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

image = Image.open("/Users/timburns/Documents/GitHub/itp/12Final/before_the_flood/assets/images/Prologue1.png")
photo = ImageTk.PhotoImage(image)
image_id = canvas.create_image(0, 0, image=photo, anchor="nw")

text_box = tk.Text(scrollable_frame, bg="white", wrap="word", height=50, width=120, font=("Courier", 14))
text_box.pack()
root.wm_attributes("-transparentcolor", "white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()