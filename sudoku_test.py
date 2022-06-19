def sudoku_test(board: list) -> str:
    '''
    takes a list of 9 x 9 x 9 integers and returns if the list is a valid sudoku board
    :param board: list of integers that represent a 9 x 9 x 9 sudoku board
    
    example of valid sudoku board:
    board = [
        [2,9,5,7,4,3,8,6,1],
        [4,3,1,8,6,5,9,2,7],
        [8,7,6,1,9,2,5,4,3],
        [3,8,7,4,5,9,2,1,6],
        [6,1,2,3,8,7,4,9,5],
        [5,4,9,2,1,6,7,3,8],
        [7,6,3,5,2,4,1,8,9],
        [9,2,8,6,7,1,3,5,4],
        [1,5,4,9,3,8,6,7,2]
    ]
    '''
    
    for row in range(0, 9):
        col_list = [board[c][row] for c in range(0, 9)]
        for n in range(1, 10):
            if board[row].count(n) != 1:
                print('invalid sudoku board in row {} number {}'.format(r, n))
                return
            elif col_list.count(n) != 1:
                print('invalid sudoku board in column {} number {}'.format(r, n))
                return

            else:
                continue

    for i in range(0, 9):
        if 0 <= i <= 2:
            row_list = [0, 1, 2]
        elif 3 <= i <= 5:
            row_list = [3, 4, 5]
        elif 6 <= i <= 8:
            row_list = [6, 7, 8]

        if i in [0, 3, 6]:
            col_list = [0, 1, 2]
        elif i in [1, 4, 7]:
            col_list = [3, 4, 5]
        elif i in [2, 5, 8]:
            col_list = [6, 7, 8]

        block_list = [board[r][c] for r in row_list for c in col_list]
        for n in range(1, 10):
            if block_list.count(n) != 1:
                print('invalid sudoku board in block {}'.format(i))
                return
            else:
                continue
                
    print('valid sudoku board')
