import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DynamicListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic List with Labels and Images")

        # Create a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Canvas widget with the scrollbar attached
        self.canvas = tk.Canvas(root, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        # Create a frame inside the canvas to hold the list items
        self.list_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.list_frame, anchor=tk.NW)

        # Simulate a list of data (labels and image paths)
        self.data_list = [
            {"label": "Item 1", "image_path": "images/Cars/New Cars/BMW M8 .png"},
            {"label": "Item 2", "image_path": "images/Cars/New Cars/Audi A8 .png"},
            {"label": "Item 3", "image_path": "images/Cars/New Cars/Audi A7.png"},
            # Add more items as needed
        ]

        # Load and display the list items
        self.load_list_items()

        # Bind the canvas to update the scrollbar when the window size changes
        self.list_frame.bind("<Configure>", self.on_frame_configure)

    def load_list_items(self):
        for item_data in self.data_list:
            label = tk.Label(self.list_frame, text=item_data["label"])
            label.pack(padx=10, pady=5, anchor=tk.W)

            image = Image.open(item_data["image_path"])
            image = image.resize((500, 300))
            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.list_frame, image=photo)
            image_label.image = photo  # Store a reference to prevent garbage collection
            image_label.pack(padx=10, pady=5, anchor=tk.W)

    def on_frame_configure(self, event):
        # Update the canvas scroll region to include the new frame size
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DynamicListApp(root)
    root.mainloop()