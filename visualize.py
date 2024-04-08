import tkinter as tk
import random

objects = []
knapsack_space = 30
COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "gold", "magenta", "pink", "cyan"]

def add_random_object():
    global objects
    print("Add Random Object")
    add_random_object_button.config(relief=tk.SUNKEN)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.RAISED)

    canvas.delete("objects")
    canvas.delete("labels")
    
    knapsack_width = 300
    knapsack_height = 100
    knapsack_x = 50
    knapsack_y = 50

    canvas.create_rectangle(knapsack_x, knapsack_y, knapsack_x + knapsack_width, knapsack_y + knapsack_height, outline="black")
    canvas.create_text(knapsack_x + knapsack_width/2, knapsack_y - 20, text=f"Capacity: {knapsack_space}", tags="labels")

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
                objects.append((x, y, size, size, weight, price))
                break

def run_bottom_up():
    global objects, knapsack_space
    print("Run Bottom Up")
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.SUNKEN)
    run_memFun_button.config(relief=tk.RAISED)

    numObjects = len(objects)
    dyPro = [[0] * (knapsack_space + 1) for x in range(numObjects + 1)]

    for i in range(1, numObjects + 1):
        for j in range(knapsack_space + 1):
            weight = objects[i - 1][4]
            price = objects[i - 1][5]
            if weight <= j:
                dyPro[i][j] = max(dyPro[i - 1][j], dyPro[i - 1][j - weight] + price)
            else:
                dyPro[i][j] = dyPro[i - 1][j]

    knapsack_objects = []
    j = knapsack_space
    for i in range(numObjects, 0, -1):
        if dyPro[i][j] != dyPro[i - 1][j]:
            knapsack_objects.append(objects[i - 1])
            j -= objects[i - 1][4]

    print("Selected objects:", knapsack_objects)
    print(len(knapsack_objects))

    knapsack_width = 300
    knapsack_height = 100
    knapsack_x = 50
    knapsack_y = 50
    x_offset = knapsack_x
    y_offset = knapsack_y

    for obj in knapsack_objects:
        x, y, size, _, _, _ = obj
        canvas.create_rectangle(x_offset, y_offset, x_offset + size, y_offset + size, fill="white", outline="black")
        canvas.create_text(x_offset + size/2, y_offset + size/2, text=f"Weight: {obj[4]}\nPrice: {obj[5]}", anchor="center")
        x_offset += size 






    
def run_memFun():
    global objects, knapsack_space
    print("Run memFun")
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.SUNKEN)

    numObjects = len(objects)

    memoryTable = [[-1] * (knapsack_space + 1) for x in range(numObjects + 1)]

    def memoryFun(i, capacity):
        if i == 0 or capacity == 0:
            return 0
        if memoryTable[i][capacity] != -1:
            return memoryTable[i][capacity]
        weight = objects[i - 1][4]
        price = objects[i - 1][5]
        if weight > capacity:
            memoryTable[i][capacity] = memoryFun(i - 1, capacity)
        else:
            memoryTable[i][capacity] = max(memoryFun(i - 1, capacity), memoryFun(i - 1, capacity - weight) + price)
        return memoryTable[i][capacity]

    priceSum = memoryFun(numObjects, knapsack_space)


    selected_objects = []
    capacity = knapsack_space
    for i in range(numObjects, 0, -1):
        if memoryFun(i, capacity) != memoryFun(i - 1, capacity):
            selected_objects.append(objects[i - 1])
            capacity -= objects[i - 1][4]

    print("Selected objects:", selected_objects)
    print("Number of selected objects:", len(selected_objects))

    knapsack_width = 300
    knapsack_height = 100
    knapsack_x = 50
    knapsack_y = 50
    x_offset = knapsack_x
    y_offset = knapsack_y

    for obj in selected_objects:
        x, y, size, _, _, _ = obj
        canvas.create_rectangle(x_offset, y_offset, x_offset + size, y_offset + size, fill="white", outline="black")
        canvas.create_text(x_offset + size / 2, y_offset + size / 2, text=f"Weight: {obj[4]}\nPrice: {obj[5]}", anchor="center")
        x_offset += size

    

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
