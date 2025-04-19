import tkinter as tk
from tkinter import ttk, messagebox


class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        self.winning_line = []
        self.buttons = {}
        self.current_turn = "X"
        self.create_frame()

    def create_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill=tk.BOTH)

        for x in range(3):
            for y in range(3):
                button = ttk.Button(frame, text="", command=lambda: self.on_button_clicked(x, y), width=6)
                button.grid(row=x, column=y, sticky="nsew")
                self.buttons[(x, y)] = button

        for i in range(3):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)

    def on_button_clicked(self, x, y):
        button = self.buttons[(x, y)]
        if button["text"] == "":
            button["text"] = self.current_turn
            if self.check_winner():
                self.show_winner()
            elif all((btn["text"] != "") for btn in self.buttons.values()):
                messagebox.showinfo("Draw", "No winners this time!")
                self.root.destroy()

            if self.current_turn == "X":
                self.current_turn = "O"
            else:
                self.current_turn = "X"

    def check_winner(self):
        b = self.buttons
        lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for line in lines:
            texts = [b[pos]["text"] for pos in line]
            if texts[0] != "" and all(t == texts[0] for t in texts):
                self.winning_line = line
                return True
        return False

    def show_winner(self):
        for x, y in self.winning_line:
            self.buttons[(x, y)].config(style="Winner.TButton")
        winner = self.current_turn
        messagebox.showinfo("Game over", f"{winner} wins!")
        self.root.destroy()

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Winner.TButton", foreground="red")
    game = TicTacToeGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
