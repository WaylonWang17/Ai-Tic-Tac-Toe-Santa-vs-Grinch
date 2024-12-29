import random
import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow to handle JPEG images

player1 = 'X'
AI = 'O'

class Board:
    def __init__(self, master):
        '''
        initializes the board class and provides its attributes
        '''
        self.master = master #tkinter window
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]] #buttons for tkinter prior to setting values
        self.counter = 0  

        self.set_window_background()
        self.load_images()
        self.initial_resize()
        self.create_buttons()
        self.configure_grid()
        self.create_status_label()

        self.replay_label = tk.Label(self.master, text="Replay", font=("Arial", 20), bg="yellow", fg="black")
        self.replay_label.grid(row=4, column=0, columnspan=3, sticky="nsew")
        self.replay_label.grid_forget()  # Hide replay label initially
        self.replay_label.bind("<Button-1>", self.replay)  # Bind replay to click event


    def set_window_background(self):
        """
        Set the background color of the window
        """
        self.master.configure(bg='red')

    def load_images(self):
        """
        Load images for Santa and Grinch (JPEG format)
        """
        self.santa_image = Image.open("C:/Users/waylo/OneDrive/projects/santa.jpg")  
        self.grinch_image = Image.open("C:/Users/waylo/OneDrive/projects/grinch.jpg")  

    def initial_resize(self):
        """
        Resize images based on initial window size
        """
        # Calculate the new size based on the window width, but ensure it's greater than 50 pixels
        self.new_size = max(self.master.winfo_width() // 3, 50)  
        self.santa_image_resized = self.resize_image(self.santa_image, self.new_size)
        self.grinch_image_resized = self.resize_image(self.grinch_image, self.new_size)

        # Convert the images to a Tkinter-compatible format
        self.santa_image_tk = ImageTk.PhotoImage(self.santa_image_resized)
        self.grinch_image_tk = ImageTk.PhotoImage(self.grinch_image_resized)

    def resize_image(self, image, size):
        """
        Resize image based on the size of the button
        """
        width, height = image.size
        aspect_ratio = width / height
        new_width = size
        new_height = int(size / aspect_ratio)
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    def create_buttons(self):
        """
        Create buttons for each square in the Tic-Tac-Toe grid
        """
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    self.buttons[i][j] = tk.Button(self.master, text=' ', width=10, height=3, bg='green', command=lambda row=i, col=j: self.player_move(row, col))
                    self.buttons[i][j].grid(row=i, column=j, sticky="nsew")
                elif j % 2 == 0 and i % 2 == 0:
                    self.buttons[i][j] = tk.Button(self.master, text=' ', width=10, height=3, bg='green', command=lambda row=i, col=j: self.player_move(row, col))
                    self.buttons[i][j].grid(row=i, column=j, sticky="nsew")
                else:
                    self.buttons[i][j] = tk.Button(self.master, text=' ', width=10, height=3, bg='red', command=lambda row=i, col=j: self.player_move(row, col))
                    self.buttons[i][j].grid(row=i, column=j, sticky="nsew")

    def configure_grid(self):
        """
        Configure the grid for responsive resizing
        """
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1, uniform="equal")
            self.master.grid_rowconfigure(i, weight=1, uniform="equal")

    def create_status_label(self):
        """
        Create a label to show whose turn it is
        """
        self.status_label = tk.Label(self.master, text="Player 1's turn", font=("Romans", 14), bg='white', fg='red')  
        self.status_label.grid(row=10, column=0, columnspan=10)

    def player_move(self, row, col):
        '''
        Everything to do with players moves and win conditions
        '''
        if self.board[row][col] == ' ':
            self.board[row][col] = player1
            self.buttons[row][col].config(image=self.santa_image_tk, text='')  
            if self.check_win():
                self.status_label.config(text="Player 1 wins!", fg='red')
                self.show_replay_label()
            elif self.is_board_full():
                self.status_label.config(text="It's a draw!", fg='black')
                self.show_replay_label()
            else:
                self.counter += 1
                self.status_label.config(text="AI's turn", fg='green')
                self.master.after(500, self.ai_move)  #delays ais movement so its more clear for player

    def ai_move(self):
        '''
        Everything to do with ai's moves and win conditions
        '''
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] == ' ':
                self.board[row][col] = AI
                self.buttons[row][col].config(image=self.grinch_image_tk, text='')  # Set the Grinch image for AI
                if self.check_win():
                    self.status_label.config(text="AI wins!", fg='green')
                    self.show_replay_label()
                elif self.is_board_full():
                    self.status_label.config(text="It's a draw!", fg='black')
                    self.show_replay_label()
                else:
                    self.counter += 1
                    self.status_label.config(text="Player 1's turn", fg='red')
                break

    def check_win(self):
        '''
        Checks to see if anybody has won yet
        '''
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True  
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True  

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True  
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True  

        return False

    def is_board_full(self):
        '''
        Checks to see if the board is full
        '''
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def end_game(self):
        '''
        Ends the game
        '''
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)  # Disable all buttons after the game ends

    def show_replay_label(self):
        '''
        Show replay label
        '''
        self.replay_label.config(font=("Roman", 30))  # Increase the font size
        self.replay_label.config(width=20, height=2)  # Increase width and height
        self.replay_label.grid(row=1, column=0, columnspan=3)  #Center it properly in the grid

    def replay(self, event=None):
        '''
        Reset board, label, etc and restart the game
        '''
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] 
        self.counter = 0  #reset counter
        self.status_label.config(text="Player 1's Turn")  #reset the status label
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(image='', text='')  #clear button images and text
        self.replay_label.grid_forget()  #hide the replay label again



def main():
    window = tk.Tk() #creates tkinter window, window = object that represents the window, tk.Tk = initializes window and lets you customize it (buttons, window size)
    window.title("Tic-Tac-Toe: Santa vs Grinch")  # set the window title to "Tic Tac Toe"
    window.geometry("1920x1080") #set size to my screen size
    game = Board(window) #creates an instance of the board class and passes window as an object

    game.initial_resize() #resize image method called for game

    window.mainloop() #responds to users actions and keeps window up and running

if __name__ == "__main__":
    main()