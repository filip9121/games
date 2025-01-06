#25 rows 25 columns, 625 pixels, 25 tiles
import tkinter as from tkinter import *
import random

ROWS =25
COLS=25
TILE_SIZE= 25


WINDOW_WIDTH= TILE_SIZE * ROWS
WINDOW_HEIGHT=TILE_SIZE*COLS

#window
window= tkinter.tk()
window.title=("snake")
window.resizable(False)



snake = [(12, 12)]  # Initial snake position
direction = (0, -1)  # Start moving upward
food = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))


def draw_tile(position, color):
    x, y = position
    x1, y1 = x * TILE_SIZE, y * TILE_SIZE
    x2, y2 = x1 + TILE_SIZE, y1 + TILE_SIZE
    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def render():
    canvas.delete("all")
    for segment in snake:
        draw_tile(segment, "green")
    
    draw_tile(food, "red")

canvas=tkinter.canvas(window,bg="gray")
window.update()
window.mainloop



render()
window.after(100, move)
window.mainloop()