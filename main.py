# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def main():
    first_board = [[], [], [], [], [], [], [], [], [], []]
    for g in range(0, 10):
        for k in range(0, 10):
            first_board[g].append(0)
            print(first_board[g][k], end=' ')
        print()
    z = (input())
    first_board[3][3] = 1
    first_board[3][4] = 1
    first_board[3][5] = 1

    first_board = dead_or_life_condition(first_board)
    z = (input())
    first_board = dead_or_life_condition(first_board)
    z = (input())
    first_board = dead_or_life_condition(first_board)
    z = (input())
    first_board = dead_or_life_condition(first_board)
    z = (input())
    first_board = dead_or_life_condition(first_board)
    z = (input())
    first_board = dead_or_life_condition(first_board)



def dead_or_life_condition(board):
    new_board = [[], [], [], [], [], [], [], [], [], []]
    for m in range(len(new_board)):
        for n in range(0, 10):
            new_board[m].append(0)

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 1:
                if board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][
                    j - 1] + \
                        board[i][j + 1] + board[i + 1][j - 1] + \
                        board[i + 1][j] + \
                        board[i + 1][j + 1] == 2:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
            elif board[i][j] == 0:
                if board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][
                    j - 1] + \
                        board[i][j + 1] + board[i + 1][j - 1] + \
                        board[i + 1][j] + \
                        board[i + 1][j + 1] == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
    for u in range(0, 10):
        for v in range(0, 10):
            print(board[u][v], end=" ")
        print()
    return new_board


def print_board(a):
    for m in range(len(a)):
        for n in range(len(a[m])):
            print(a[m][n], end=' ')
        print()



if __name__ == "__main__":
    main()
