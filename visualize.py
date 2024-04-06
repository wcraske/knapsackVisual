import tkinter as tk
import random

def add_random_object():
    print("Add Random Object")
    add_random_object_button.config(relief=tk.SUNKEN)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.RAISED)

    canvas.delete("objects")
    canvas.delete("labels")
    
    knapsack_width = 300
    knapsack_height = 300
    knapsack_x = 50
    knapsack_y = 50
    knapsack_capacity = 50

    canvas.create_rectangle(knapsack_x, knapsack_y, knapsack_x + knapsack_width, knapsack_y + knapsack_height, outline="black")
    canvas.create_text(knapsack_x + knapsack_width/2, knapsack_y - 20, text=f"Capacity: {knapsack_capacity}", tags="labels")

    objects = [] 
    COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "gold", "magenta", "pink", "cyan"]

    for i in range(10):
        while True:
            x = random.randint(400, 700)
            y = random.randint(100, 500)
            size = random.randint(30, 80)
            weight = random.randint(1, 10)
            price = size * 2  
            overlap = False

            for obj in objects:
                if (x < obj[0] + obj[2] and x + size > obj[0] and y < obj[1] + obj[3] and y + size > obj[1]):
                    overlap = True
                    break

            if not overlap:
                color = COLORS.pop()
                canvas.create_rectangle(x, y, x + size, y + size, fill=color, tags="objects")
                canvas.create_text(x + size/2, y + size/2, text=f"Weight: {weight}\nPrice: {price}", tags="labels")
                objects.append((x, y, size, size))
                break

def run_bottom_up():
    print("Run Bottom Up")
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.SUNKEN)
    run_memFun_button.config(relief=tk.RAISED)

def run_memFun():
    print("Run memFun")
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.SUNKEN)

root = tk.Tk()
root.title("Visualizer")
root.geometry("800x600")

button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

add_random_object_button = tk.Button(button_frame, text="Add Random Objects", command=add_random_object, relief=tk.RAISED)
add_random_object_button.pack(side="left", padx=5, pady=5)

run_bottom_up_button = tk.Button(button_frame, text="Run Bottom Up", command=run_bottom_up, relief=tk.RAISED)
run_bottom_up_button.pack(side="left", padx=5, pady=5)

run_memFun_button = tk.Button(button_frame, text="Run memFun", command=run_memFun, relief=tk.RAISED)
run_memFun_button.pack(side="left", padx=5, pady=5)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

root.mainloop()
