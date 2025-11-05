def is_safe(board, row, col):
    # Ellenőrizzük, hogy van-e másik királynő ugyanabban az oszlopban vagy átlókban.
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n, row=0, board=None):
    if board is None:
        board = [-1] * n  # Kezdetben minden sor üres.


    if row == n:  # Minden királynőt elhelyeztünk.
        print([pos + 1 for pos in board])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Királynő elhelyezése.
            solve_n_queens(n, row + 1, board)
            board[row] = -1  # Visszalépés.


# Meghívás 8×8-as táblára:
solve_n_queens(8)
