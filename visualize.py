import tkinter as tk

def add_random_object():
    print("Add Random Object")
    add_random_object_button.config(relief=tk.SUNKEN)
    run_bottom_up_button.config(relief=tk.RAISED)
    run_memFun_button.config(relief=tk.RAISED)

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
