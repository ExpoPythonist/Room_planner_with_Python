import tkinter as tk


class RoomDesigner:
    def __init__(self, master):
        self.master = master
        self.master.title("Room Designer")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
        self.furniture_options = ["Chair", "Table", "Bed"]
        self.selected_furniture = tk.StringVar()
        self.selected_furniture.set(self.furniture_options[0])
        self.floor_color = "white"  # Default floor color
        self.create_ui()

    def create_ui(self):
        # Furniture selection dropdown
        tk.Label(self.master, text="Select Furniture:").pack()
        furniture_menu = tk.OptionMenu(self.master, self.selected_furniture, *self.furniture_options)
        furniture_menu.pack()

        # Floor color selection
        tk.Label(self.master, text="Select Floor Color:").pack()
        tk.Button(self.master, text="White", command=lambda: self.change_floor_color("white")).pack()
        tk.Button(self.master, text="Gray", command=lambda: self.change_floor_color("gray")).pack()
        tk.Button(self.master, text="Brown", command=lambda: self.change_floor_color("brown")).pack()

        # Buttons
        tk.Button(self.master, text="Place Furniture", command=self.place_furniture).pack()
        tk.Button(self.master, text="Clear All", command=self.clear_all).pack()

        # Canvas bindings
        self.canvas.bind("<Button-1>", self.place_item)

    def place_furniture(self):
        furniture = self.selected_furniture.get()
        if furniture == "Chair":
            self.canvas.create_rectangle(50, 50, 100, 100, fill="brown")
        elif furniture == "Table":
            self.canvas.create_rectangle(150, 150, 250, 200, fill="gray")
        elif furniture == "Bed":
            self.canvas.create_rectangle(300, 300, 450, 350, fill="blue")

    def clear_all(self):
        self.canvas.delete("all")

    def place_item(self, event):
        x, y = event.x, event.y
        furniture = self.selected_furniture.get()
        if furniture == "Chair":
            self.canvas.create_rectangle(x - 25, y - 25, x + 25, y + 25, fill="brown")
        elif furniture == "Table":
            self.canvas.create_rectangle(x - 50, y - 25, x + 50, y + 25, fill="gray")
        elif furniture == "Bed":
            self.canvas.create_rectangle(x - 75, y - 25, x + 75, y + 25, fill="blue")

    def change_floor_color(self, color):
        self.floor_color = color
        self.canvas.config(bg=self.floor_color)


def main():
    root = tk.Tk()
    app = RoomDesigner(root)
    root.mainloop()


if __name__ == "__main__":
    main()
