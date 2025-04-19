import tkinter as tk
from tkinter import ttk


def create_game_frame(master: tk.Tk):
    frame = tk.Frame(master)

    frame.grid_configure(padx=5, pady=5, columnspan=3, rowspan=3)

    cells = {
        (x, y): ttk.Button(frame, text=f"{x} {y}", command=lambda: print(x, y))
        for x, y in range(3, 3)
    }

    for (x, y), cell in cells.items():
        cell.grid(column=x, row=y)

    return frame


def main():
    root = tk.Tk()
    root.resizable = False
    root.size = (500, 500)
    root.title = "Tic tac toe"

    frame = create_game_frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()