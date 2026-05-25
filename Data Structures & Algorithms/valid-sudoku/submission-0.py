class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        board_w = 9
        board_h = 9
        # ======= scan rows ======== 
        for r in range(board_h):
            num_list = [0] * board_w
            for c in range(board_w):
                if board[r][c] == ".":
                    continue
                idx = int(board[r][c])-1
                if num_list[idx] == 1:
                    return False
                num_list[idx] = 1 
        # ======= scan cols ==========
        for c in range(board_w):
            num_list = [0] * board_h
            for r in range(board_h):
                if board[r][c] == ".":
                    continue
                idx = int(board[r][c])-1
                if num_list[idx] == 1:
                    return False
                num_list[idx] = 1
        # ======== scan 3X3 ===========
        for b_r in range(0, board_w, 3):
            for b_c in range(0, board_h, 3):
                num_list = [0] * board_h
                for r in range(b_r, b_r+3):
                    for c in range(b_c, b_c+3):
                        if board[r][c] == ".":
                            continue
                        idx = int(board[r][c])-1
                        if num_list[idx] == 1:
                            return False
                        num_list[idx] = 1        
        return True      



