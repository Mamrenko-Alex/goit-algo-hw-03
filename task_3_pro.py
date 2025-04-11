import tkinter as tk
import time

DISK_HEIGHT = 20

class HanoiVisualizer:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack()
        self.towers = [[], [], []]
        self.disk_ids = {}
        self.peg_positions = [100, 300, 500]
        self.base_y = 250
        self.move_count = 0
        self.step_text = self.canvas.create_text(10, 10, anchor="nw", text="Moves: 0", font=("Arial", 14), fill="black")

        self.draw_pegs()
        self.init_disks()
        self.root.update()

    def draw_pegs(self):
        for x in self.peg_positions:
            self.canvas.create_rectangle(x - 5, 100, x + 5, 250, fill="black")

    def init_disks(self):
        for i in range(self.num_disks, 0, -1):
            width = i * 20
            x = self.peg_positions[0]
            y = self.base_y - len(self.towers[0]) * DISK_HEIGHT
            disk_id = self.canvas.create_rectangle(
                x - width, y - DISK_HEIGHT, x + width, y,
                fill="red"
            )
            self.towers[0].append(i)
            self.disk_ids[i] = disk_id

    def move_disk(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)
        disk_id = self.disk_ids[disk]

        x = self.peg_positions[to_tower]
        y = self.base_y - (len(self.towers[to_tower]) - 1) * DISK_HEIGHT

        self.canvas.coords(disk_id, x - disk*20, y - DISK_HEIGHT, x + disk*20, y)
        self.move_count += 1
        self.canvas.itemconfig(self.step_text, text=f"Moves: {self.move_count}")
        self.root.update()
        time.sleep(0.5)

    def solve(self, n, source, auxiliary, target):
        if n == 1:
            self.move_disk(source, target)
        else:
            self.solve(n - 1, source, target, auxiliary)
            self.move_disk(source, target)
            self.solve(n - 1, auxiliary, source, target)

def start_menu():
    try:
        num_disks = int(entry.get())
        if num_disks < 1:
            raise ValueError("Number must be at least 1")
    except ValueError:
        error_label.config(text="Enter a valid number ≥ 1")
        return

    menu.destroy()

    root = tk.Tk()
    root.title("Tower of Hanoi")
    visualizer = HanoiVisualizer(root, num_disks)
    root.after(1000, lambda: visualizer.solve(num_disks, 0, 1, 2))
    root.mainloop()

menu = tk.Tk()
menu.title("Tower of Hanoi Setup")
menu.geometry("300x150")

label = tk.Label(menu, text="Enter number of disks:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(menu, justify="center", font=("Arial", 12))
entry.pack()

error_label = tk.Label(menu, text="", fg="red", font=("Arial", 10))
error_label.pack()

start_button = tk.Button(menu, text="Start Game", command=start_menu, font=("Arial", 12))
start_button.pack(pady=10)

menu.mainloop()
