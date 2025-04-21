import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        self.header = None
        self.buttons = {}
        self.current_turn = "✕"
        self.create_styles()
        self.create_gui()

    def create_styles(self):
        style = ttk.Style(self.root)


        style.configure(
            "MyButton.TButton",
            font=("Segoe UI", 28, "bold"),
            background="#c4c4c4",
            padding=0
        )
        style.map(
            "MyButton.TButton",
            foreground=[("disabled", "#666")]
        )
        style.configure(
            "MyLabel.TLabel",
            font=("Segoe UI", 28, "bold"),
            foreground="#222"
        )

    def create_gui(self):
        self.header = ttk.Label(self.root, text=f"Turn: {self.current_turn}", style="MyLabel.TLabel")
        self.header.pack(pady=(16, 8))

        frame = ttk.Frame(self.root, padding=8)
        frame.pack(expand=True, fill=tk.BOTH)

        for x in range(3):
            for y in range(3):
                button = ttk.Button(
                    frame,
                    text="",
                    command=lambda xx=x, yy=y: self.on_button_clicked(xx, yy),
                    style="MyButton.TButton"
                )
                button.grid(row=x, column=y, sticky="nsew", padx=4, pady=4)
                self.buttons[(x, y)] = button

        for i in range(3):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)

    def on_button_clicked(self, x, y):
        button = self.buttons[(x, y)]
        if button["text"] == "":
            button["text"] = self.current_turn
            button.state(["disabled"])
            if self.check_winner() or self.check_draw():
                return
            self.toggle_turn()
            self.header.config(text=f"Turn: {self.current_turn}")

    def check_winner(self):
        b = self.buttons
        winning_lines = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for line in winning_lines:
            texts = [b[pos]["text"] for pos in line]
            if texts[0] != "" and all(t == texts[0] for t in texts):
                messagebox.showinfo("Game over", f"{self.current_turn} wins!")
                self.root.destroy()
                return True
        return False

    def check_draw(self):
        if all((b["text"] != "") for b in self.buttons.values()):
            messagebox.showinfo("Draw", "No winner!")
            self.root.destroy()
            return True
        return False

    def toggle_turn(self):
        self.current_turn = ("◯" if self.current_turn == "✕" else "✕")


def main():
    root = tk.Tk()
    TicTacToeGame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
