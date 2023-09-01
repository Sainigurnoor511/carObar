import tkinter as tk
from tkinter import ttk

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.itemconfigure(scrollable_frame, width=canvas.winfo_width())

# Create the main window
window = tk.Tk()
window.title("Two Frames with Scrolling")
window.geometry("700x1000")

# Create the first frame at the top
frame1 = tk.Frame(window, height=200, width=700, bg="lightgray")
frame1.pack(side=tk.TOP, fill=tk.X)

# Create a canvas to enable scrolling for the second frame
canvas = tk.Canvas(window, height=800, width=700)
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create the second frame inside the canvas
scrollable_frame = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

# Add widgets to the second frame (scrollable frame)
for i in range(30):
    label = tk.Label(scrollable_frame, text=f"Label {i}")
    label.pack(pady=5)

# Bind the canvas scroll region and frame resize
canvas.bind("<Configure>", on_frame_configure)
scrollable_frame.bind("<Configure>", on_frame_configure)

window.mainloop()
