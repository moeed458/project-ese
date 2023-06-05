import tkinter as tk #importing tkinter
from tkinter import messagebox

class TicTacToeGUI:  #defining the class
    def __init__(self): #defining the function that initialize
        self.board = [' '] * 10
        self.current_player = 'X'
        self.games_played = 0
###MAKING CODE THAT CONFIGURES THE WINDOW
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")

        self.buttons = []
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.pack()
#DEFINING THE BUTTON STYLE
        button_style = {
            'font': ('Helvetica', 20),
            'width': 6,
            'height': 2,
            'relief': 'groove',
            'bg': 'light blue'  # Button color
        }
#MAKINGG THE LOOP FOR NUMBER OF ITERATIONS THAT CONCIDES WITH THE PLAYER TRACK RECORD
        for i in range(1, 10):
            button = tk.Button(self.grid_frame, text=' ', **button_style,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.window, text="Reset", font=("Helvetica", 16), width=10, command=self.reset_game)
        self.reset_button.pack(pady=10)

        self.status_label = tk.Label(self.window, text="Player X's turn", font=("Helvetica", 16))
        self.status_label.pack()

        self.games_label = tk.Label(self.window, text="Games Played: 0", font=("Helvetica", 16))
        self.games_label.pack()


#FUNCTION THAT KEEP THE RECORD OF PPLAYER POSITION
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position-1].config(text=self.current_player, state='disabled')
#MAKING OF CONDITION OF PLACE OF PLAYER
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.games_played += 1
                self.update_games_label()
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.games_played += 1
                self.update_games_label()
                self.reset_game()
            else:
                self.switch_player()
                self.update_status_label()
#MAKING OF FUNCTION THAT SWITCH THE PLAYER
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
#FUNCTION THAT SPECIFY THE WINNNER BY KEEPING RECORD OF BOTH PLAYERS BY THIER GIVEN INPUTS
    def check_winner(self):
        winning_positions = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)  # Diagonals
        ]
#LOOP THAT ITERATE OVER THE GIVEN MATRIX FOR PLAYERS
        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != ' ':
                return True
        return False
#DEFINING THAT FUNCTION THAT RUN ALONG WITH THE CODE THAT KEEP TRACK OF MOVES OF BOTH PLAYER
    def check_draw(self):
        return ' ' not in self.board[1:]
#THIS FUNCTION RESET THE GAME RECORD IF PLAYER PRESSS THE RESET BUTTON
    def reset_game(self):
        self.board = [' '] * 10
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ', state='normal')
#FUNCTION THAT DISPLAYS THE MESSAGE AND ITERATE OVER THE TURN OF BOTH PLAYER
    def update_status_label(self):
        self.status_label.config(text=f"Player {self.current_player}'s turn")
    def update_games_label(self):
        self.games_label.config(text=f"Games Played: {self.games_played}")
    def run(self):
        self.window.mainloop()
# Create an instance of the TicTacToeGUI class and run the game
game = TicTacToeGUI()
game.run()
