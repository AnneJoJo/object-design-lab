import random

class tic_tac_toe:
    def __init__(self):
        # initailize the board
        self.board = [[" " for i in range(3)] for j in range(3)]
        self.computer = ""
        self.player = ""

    def who_go_first(self,answer):
        # if player choose No, Computer goes first
        if answer in ['N','n']:
            self.get_computerplayer_move()

    def decide_letter(self,c):
        # Let player choose which letter he/she wants to use
        if c == "X":
            self.computer = "O"
            self.player = "X"
        else:
            self.computer = "X"
            self.player = "O"

    def show_the_board(self):
        # show the current board
        print(self.board)

    def check_can_place(self,curr_x,curr_y):
        # check if the place is available
        if self.board[curr_x][curr_y] == "X" or self.board[curr_x][curr_y] == "O" :
            return False
        else:
            return True

    def get_player_move(self,x,y):
        player_letter = self.player

        self.board[x][y] = player_letter
        if self.isWin(player_letter):
                return True

        return False
    def random_place(self):

        return random.choice(self.get_cur_avaliable_place())

    def get_cur_avaliable_place(self):
        possible_place = []
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == " ":
                    possible_place.append([r, c])
        return possible_place


    def get_computerplayer_move(self):
        # this computer need to check the current status and make the desicion for next move
        # check if we can win in next turn
        computer_letter = self.computer
        player_letter = self.player

        available_place = self.get_cur_avaliable_place()
        for each_cell in available_place:
            x = each_cell[0]
            y = each_cell[1]
            self.board[x][y] = computer_letter
            if self.isWin(computer_letter):
                print("aaa")
                return True
            else:
                self.board[x][y] = " "
        # if player will win in next setp block it
        for each_cell in available_place:
            x = each_cell[0]
            y = each_cell[1]
            self.board[x][y] = player_letter
            if self.isWin(player_letter):
                self.board[x][y] = computer_letter
                break
            else:
                self.board[x][y] = " "
        # otherwise random pick a place
        rand_place = self.random_place()
        self.board[rand_place[0]][rand_place[1]] = computer_letter


    def isWin(self,letter):
        # check the row:
        for i in range(3):
            if self.board[i][0] == letter and self.board[i][1] == letter and self.board[i][2] == letter:
                return True
        # check the col:
        for j in range(3):
            if self.board[0][j] == letter and self.board[1][j] == letter and self.board[2][j] == letter:
                return True
        # check the diag:
        if self.board[0][0] == letter and self.board[1][1] == letter and self.board[2][2] == letter:
            return True
        if self.board[0][2] == letter and self.board[1][1] == letter and self.board[2][0] == letter:
            return True

        return False

    def check_board_full(self):
        # use to check tie
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.check_can_place(r,c):
                    return False
        return True

def main():
    while True:
        game = tic_tac_toe()
        print("welcome to play the Tic Tac Toe Game")
        print("Choose the letter you want to use X or O")
        letter_for_player = input()
        game.decide_letter(letter_for_player)
        print("Do you want to go first? Y?N")
        ans = input()

        if ans in ["N","n"]:
            game.get_computerplayer_move()

        while True:
            if game.check_board_full():
                print("Tie")
                break
            game.show_the_board()

            while True:
                print("place the place you want to go x,y")
                x = int(input())
                y = int(input())
                if x > 2 or y > 2 or x < 0 or y < 0:
                    
                    print("please enter valid position from 0 ~ 2")
                    continue
                if game.check_can_place(x,y):
                    break
                else:
                    print("you place invalid!")
            if game.get_player_move(x,y):
                game.show_the_board()
                print("player Win")
                break

            if game.get_computerplayer_move():
                game.show_the_board()
                print("computer Win")
                break
        print("Do you want to play again? Y/N")
        ans = input()
        if ans in ["N","n"]:
            break


if __name__ == "__main__":
    main()

