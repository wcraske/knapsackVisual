import tkinter as tk
import random
import math

def add_random_object():
 

def activate_add_random_object():
    canvas.bind("<Button-1>", add_random_object)
    canvas.unbind("<Button-3>")
    add_random_object_button.config(relief=tk.SUNKEN)
    run_algorithm_button.config(relief=tk.RAISED)

def activate_run_algorithm():
    canvas.unbind("<Button-1>")
    canvas.unbind("<ButtonRelease-1>")
    run_algorithm_button.config(relief=tk.SUNKEN)
    add_random_object_button.config(relief=tk.RAISED)

root = tk.Tk()
root.title("Visualizer")
root.geometry("800x600")

button_frame = tk.Frame(root)
button_frame.pack(side="top", fill="x")

add_random_object_button = tk.Button(button_frame, text="Add Random Object", command=activate_add_random_object, relief=tk.RAISED)
add_random_object_button.pack(side="left", padx=5, pady=5)

run_algorithm_button = tk.Button(button_frame, text="Run Algorithm", command=activate_run_algorithm, relief=tk.RAISED)
run_algorithm_button.pack(side="left", padx=5, pady=5)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

root.mainloop()
