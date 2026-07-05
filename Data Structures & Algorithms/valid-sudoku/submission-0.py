from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                box_id = (i//3, j//3)

                if board[i][j] == ".":
                    continue

                if board[i][j] in row_check[i]:
                    return False
                elif board[i][j] in col_check[j]:
                    return False
                elif board[i][j] in box_check[box_id]:
                    return False
                else:
                    row_check[i].add(board[i][j])
                    col_check[j].add(board[i][j])
                    box_check[box_id].add(board[i][j])

        return True