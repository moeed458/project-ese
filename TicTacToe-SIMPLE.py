import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self):
        self.board = [' '] * 10
        self.current_player = 'X'

        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Load and display the logo image
        logo_image = tk.PhotoImage(file="2.2.jpg")
        logo_label = tk.Label(self.window, image=logo_image)
        logo_label.pack()

        self.buttons = []

        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack()

        for i in range(1, 10):
            button = tk.Button(self.grid_frame, text=' ', font=("Helvetica", 20), padx=20, pady=20,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
            self.buttons.append(button)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position - 1].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def check_winner(self):
        winning_positions = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)  # Diagonals
        ]

        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != ' ':
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board[1:]

    def reset_game(self):
        self.board = [' '] * 10
        self.current_player = 'X'

        for button in self.buttons:
            button.config(text=' ')

    def run(self):
        self.window.mainloop()


# Create an instance of the TicTacToeGUI class and run the game
game = TicTacToeGUI()
game.run()
