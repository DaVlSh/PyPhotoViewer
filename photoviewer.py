import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.canvas = tk.Canvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = None
        self.photo = None

        self.scale = 1.0
        self.image_index = 0

        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.file_menu.add_command(label="Exit", command=root.quit)

        self.root.bind("<MouseWheel>", self.zoom)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("images", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
        )
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()


    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image.resize(
                (int(self.image.width * self.scale), int(self.image.height * self.scale)),
                Image.ANTIALIAS
            ))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def zoom(self, event):
        if event.delta > 0:
            self.scale *= 1.1
        elif event.delta < 0:
            self.scale /= 1.1
        self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
