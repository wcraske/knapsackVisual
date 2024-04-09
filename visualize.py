import tkinter as tk
import random
#import libraries for visualization and randomness

#initializing list and colours of objects as well as capacity for knapsack
objects = []
knapsack_space = 30
COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "gold", "magenta", "pink", "cyan"]

#function to add random objects to the canvas
def add_random_object():
    global objects
    print("Add Random Object")
    #button logic
    add_random_object_button.config(relief=tk.SUNKEN)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.RAISED)

    #incase of rerun, clear the canvas
    canvas.delete("objects")
    canvas.delete("labels")
    
    #defining the dimensions and position of the knapsack that is drawn
    knapsack_width = 370
    knapsack_height = 80
    knapsack_x = 50
    knapsack_y = 50

    #drawing the knapsack
    canvas.create_rectangle(knapsack_x, knapsack_y, knapsack_x + knapsack_width, knapsack_y + knapsack_height, outline="black")
    canvas.create_text(knapsack_x + knapsack_width/2, knapsack_y - 20, text=f"Capacity: {knapsack_space}", tags="labels")

    #creating 10 random objects with varying size and price
    for i in range(10):
        while True:
            x = random.randint(400, 700)
            y = random.randint(100, 500)
            size = random.randint(30, 80)
            weight = random.randint(1, 10)
            price = size * 2  
            overlap = False

            #logic to make sure that the positions of the drawn rectangles do not overlap
            for obj in objects:
                if (x < obj[0] + obj[2] and x + size > obj[0] and y < obj[1] + obj[3] and y + size > obj[1]):
                    overlap = True
                    break
            #if they dont overlap, pop a colour from the list so they are all separate. 
            #add the object with its qualities to the list, and drawing them
            if not overlap:
                color = COLORS.pop()
                canvas.create_rectangle(x, y, x + size, y + size, fill=color, tags="objects")
                canvas.create_text(x + size/2, y + size/2, text=f"Weight: {weight}\nPrice: {price}", tags="labels")
                objects.append((x, y, size, size, weight, price))
                break


#function that runs the bottom up algorithm
def run_bottom_up():
    global objects, knapsack_space
    #button logic
    print("Run Bottom Up")
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.SUNKEN)
    run_memFun_button.config(relief=tk.RAISED)

    #gets the number of objects, then creates a 2D list for our dynamic programming
    numObjects = len(objects)
    #this 2D list has the dimensions of the amount of objects +1 by the knapsack space + 1. the values are all initialized to 0
    #the list stores the results of the dynamic programming
    dyPro = [[0] * (knapsack_space + 1) for x in range(numObjects + 1)]

    #loop through each object and each knapsack space
    for i in range(1, numObjects + 1):
        for j in range(knapsack_space + 1):
            #calculate the weight and price of the object
            weight = objects[i - 1][4]
            price = objects[i - 1][5]
            #check if the weight of the object is less or equal to the capacity
            if weight <= j:
                #then calculate and assign the max value between the list currently, or the list with the object
                dyPro[i][j] = max(dyPro[i - 1][j], dyPro[i - 1][j - weight] + price)
            else:#if weight of the object is greater than the knapsacks capacity, do not include it
                dyPro[i][j] = dyPro[i - 1][j]

    #create empty list to hold the objects in the knapsack
    knapsack_objects = []
    #sets the capacity of knapsack to j
    j = knapsack_space
    #iterate through the objects in reverse to construct the list of selected items
    for i in range(numObjects, 0, -1):
        #checks value stored is different than object before it, if they are different the current object, append it to the list
        if dyPro[i][j] != dyPro[i - 1][j]:
            knapsack_objects.append(objects[i - 1])
            #reduce space of the given capacity
            j -= objects[i - 1][4]

    print("Selected objects:", knapsack_objects)
    print("Total price:", dyPro[numObjects][knapsack_space]) 


    #redefines the knapsack width and position to visulaize the end result
    knapsack_width = 300
    knapsack_height = 100
    knapsack_x = 50
    knapsack_y = 50
    x_offset = knapsack_x
    y_offset = knapsack_y

    #iterate through the selected objects and place them in the dimensions of the knapsack side by side
    for obj in knapsack_objects:
        x, y, size, _, _, _ = obj
        canvas.create_rectangle(x_offset, y_offset, x_offset + size, y_offset + size, fill="white", outline="black")
        canvas.create_text(x_offset + size/2, y_offset + size/2, text=f"Weight: {obj[4]}\nPrice: {obj[5]}", anchor="center")
        x_offset += size 


#function for memory function algorithm
def run_memFun():
    global objects, knapsack_space
    print("Run memFun")
    #button logic
    add_random_object_button.config(relief=tk.RAISED)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.SUNKEN)

    #get amount of objects
    numObjects = len(objects)

    #create a table for memory function that has dimensions of knapsack space and the number of objects, then fill with -1
    #the -1 indicates the algorithm hasnt solved it yet
    memoryTable = [[-1] * (knapsack_space + 1) for x in range(numObjects + 1)]

    #create recursive function to calculate the price
    def memoryFun(i, capacity):
        #base case if there are no more objects left in list, or if the knapsack is at capacity
        if i == 0 or capacity == 0:
            return 0
        #if the value at the current memory table has already been computed, return to avoid redundancy
        if memoryTable[i][capacity] != -1:
            return memoryTable[i][capacity]
        #calculate weight and price
        weight = objects[i - 1][4]
        price = objects[i - 1][5]
        #if weight is less than capacity, move to the next object by recursively calling itself
        if weight > capacity:
            memoryTable[i][capacity] = memoryFun(i - 1, capacity)
        #if weight is less or equal, set the value in the table as the max value between the table, or the current object by recursively calling
        else:
            memoryTable[i][capacity] = max(memoryFun(i - 1, capacity), memoryFun(i - 1, capacity - weight) + price)
        return memoryTable[i][capacity]

    #calculate the price of the knapsacks
    priceSum = memoryFun(numObjects, knapsack_space)

    #again iterate in reverse to construct the list
    selected_objects_mem = []
    capacity = knapsack_space
    for i in range(numObjects, 0, -1):
        #ihecks value stored is different than object before it, if they are different the current object, append it to the list
        if memoryFun(i, capacity) != memoryFun(i - 1, capacity):
            selected_objects_mem.append(objects[i - 1])
            #reduce total capacity by the objects weight
            capacity -= objects[i - 1][4]

    print("Selected objects:", selected_objects_mem)
    print("Number of selected objects:", len(selected_objects_mem))
    print("Total price:", priceSum) 

    #again define knapsack dimensions
    knapsack_width = 300
    knapsack_height = 100
    knapsack_x = 50
    knapsack_y = 50
    x_offset = knapsack_x
    y_offset = knapsack_y

    #iterate through selected objects list and create the objects in the knapsack
    for obj in selected_objects_mem:
        x, y, size, _, _, _ = obj
        canvas.create_rectangle(x_offset, y_offset, x_offset + size, y_offset + size, fill="white", outline="black")
        canvas.create_text(x_offset + size / 2, y_offset + size / 2, text=f"Weight: {obj[4]}\nPrice: {obj[5]}", anchor="center")
        x_offset += size
    

#create window for gui
root = tk.Tk()
root.title("Visualizer")
root.geometry("800x600")
#create buttons for each option
button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

add_random_object_button = tk.Button(button_frame, text="Add Random Objects", command=add_random_object, relief=tk.RAISED)
add_random_object_button.pack(side="left", padx=5, pady=5)

run_bottom_up_button = tk.Button(button_frame, text="Run Bottom Up", command=run_bottom_up, relief=tk.RAISED)
run_bottom_up_button.pack(side="left", padx=5, pady=5)

run_memFun_button = tk.Button(button_frame, text="Run memory function", command=run_memFun, relief=tk.RAISED)
run_memFun_button.pack(side="left", padx=5, pady=5)

#create canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

root.mainloop()
